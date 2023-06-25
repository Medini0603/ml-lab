# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris

# class LDA:
#     def __init__(self, n_components=None):
#         self.n_components = n_components
#         self.eig_vectors = None
    
#     def transform(self,X,y):
#         height, width = X.shape
#         unique_classes = np.unique(y)
#         num_classes = len(unique_classes)

#         scatter_t = np.cov(X.T)*(height - 1)
#         scatter_w = 0
#         for i in range(num_classes):
#             class_items = np.flatnonzero(y == unique_classes[i])
#             scatter_w = scatter_w + np.cov(X[class_items].T) * (len(class_items)-1)
        
#         scatter_b = scatter_t - scatter_w
#         _, eig_vectors = np.linalg.eigh(np.linalg.pinv(scatter_w).dot(scatter_b))
#         print(eig_vectors.shape)
#         pc = X.dot(eig_vectors[:,::-1][:,:self.n_components])
#         print(pc.shape)

#         if self.n_components == 2:
#             if y is None:
#                 plt.scatter(pc[:,0],pc[:,1])
#             else:
#                 colors = ['r','g','b']
#                 labels = np.unique(y)
#                 for color, label in zip(colors, labels):
#                     class_data = pc[np.flatnonzero(y==label)]
#                     plt.scatter(class_data[:,0],class_data[:,1],c=color)
#             plt.show()
#         return pc

# LDA_obj = LDA(n_components=2)
# data = load_iris()
# X, y = data.data, data.target
# X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2)

# LDA_object = LDA(n_components=2)
# X_train_modified = LDA_object.transform(X_train, Y_train)

# print("Original Data Size:",X_train.shape, "\nModified Data Size:", X_train_modified.shape)

import numpy as np
class LDA:

    def __init__(self, n):
        self.n = n
        self.ld = None

    def fit(self, X, y):
        features = X.shape[1]
        labels = np.unique(y)
        mean = np.mean(X, axis=0)
        SW = np.zeros((features, features))
        SB = np.zeros((features, features))
        for c in labels:
            X_c = X[y == c]
            mean_c = np.mean(X_c, axis=0)
            SW += (X_c - mean_c).T.dot((X_c - mean_c))
            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean).reshape(features, 1)
            SB += n_c * (mean_diff).dot(mean_diff.T)


        A = np.linalg.inv(SW).dot(SB)
        eval, evec = np.linalg.eig(A)
        evec = evec.T
        idxs = np.argsort(abs(eval))[::-1]
        eval = eval[idxs]
        evec = evec[idxs]
        self.ld = evec[0:self.n]

    def transform(self, X):
        # project data
        return np.dot(X, self.ld.T)

import matplotlib.pyplot as plt
from sklearn import datasets
data=datasets.load_iris()
X=data.data
y=data.target
lda=LDA(2)
lda.fit(X,y)
X_projected = lda.transform(X)
print(X.shape)
print(X_projected.shape)
x1=X_projected[:,0]
x2=X_projected[:,1]
plt.scatter(x1,x2,c=y,cmap="viridis")
plt.xlabel("Principal component 1")
plt.ylabel("Principal component 2")
# plt.colorbar()
plt.show()