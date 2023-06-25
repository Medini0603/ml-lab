import math
MAX=10000
MIN=-10000

def albeta(d,n,maxplayer,score,a,b):
    if(d==math.log(len(score),2)):
        return score[n]
    
    if(maxplayer):
        best=MIN
        for i in range(0,2):
            val=albeta(d+1,n*2+i,False,score,a,b)
            best=max(val,best)
            a=max(a,best)

            if(b<=a):
                break
        return best
    else:
        best=MAX
        for i in range(0,2):
            val=albeta(d+1,n*2+i,True,score,a,b)
            best=min(val,best)
            b=min(b,best)

            if(b<=a):
                break
        return best
    
values = [3, 5, 6, 9, 1, 2, 0, -1] 
scores=[3,5,2,9,12,5,23,23]

print("The optimal value is :", albeta(0, 0, True, scores, MIN, MAX))