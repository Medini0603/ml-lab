import math
MAX=10000
MIN=-10000
def minimax(d,n,maxturn,score,t):
    if(d==t):
        return score[n]
    
    if(maxturn):
        return max(minimax(d+1,n*2,False,score,t),minimax(d+1,n*2+1,False,score,t))
    else:
        return min(minimax(d+1,n*2,True,score,t),minimax(d+1,n*2+1,True,score,t))
    

scores=[3,5,2,9,12,5,23,23]
values = [3, 5, 6, 9, 1, 2, 0, -1] 
t=math.log(len(scores),2)


print("optimum val = ",minimax(0,0,True,scores,t))