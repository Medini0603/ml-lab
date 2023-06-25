import pandas as pd
import numpy as np


df = pd.read_csv('titanic.csv')

df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})

X = df.drop('Survived', axis=1)
y = df['Survived']

def _gaussian_pdf(x, mean, std):
        exponent = np.exp(-((x - mean) ** 2) / (2 * std ** 2))
        return (1 / (np.sqrt(2 * np.pi) * std)) * exponent

class NaiveBayesClassifier:
    def __init__(self):
        self.prior = {}
        self.conditional = {}

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)

        # Compute class priors
        for c in self.classes:
            self.prior[c] = np.mean(y == c)

        # Compute conditional probabilities
        for feature in X.columns:
            self.conditional[feature] = {}
            for c in self.classes:
                feature_values = X[feature][y == c]
                self.conditional[feature][c] = {
                    'mean': np.mean(feature_values),
                    'std': np.std(feature_values)
                }

    def predict(self, X):
        y_pred = []
        for _, sample in X.iterrows():
            probabilities = {}
            for c in self.classes:
                probabilities[c] = self.prior[c]
                for feature in X.columns:
                    mean = self.conditional[feature][c]['mean']
                    std = self.conditional[feature][c]['std']
                    x = sample[feature]
                    probabilities[c] *= _gaussian_pdf(x, mean, std)
            y_pred.append(max(probabilities, key=probabilities.get))
        return y_pred


# Instantiate and train the Naive Bayes classifier
classifier = NaiveBayesClassifier()
classifier.fit(X, y)

# Predict the target variable
y_pred = classifier.predict(X)

# Calculate accuracy
accuracy = np.mean(y_pred == y)
print("Accuracy:", accuracy)