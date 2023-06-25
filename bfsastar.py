def inputgraph():
    v=int(input("Enter number of vertices in graph "))
    h=[0]*v
    print("Enter hueristic of each edge ")
    for i in range(v):
        h[i]=int(input())
    
    n=int(input("Enter the number of edges "))
    e=[]*n

    print("Enter the edges ")
    for i in range(n):
        x=int(input("Enter v1 "))
        y=int(input("Enter v2 "))
        d=int(input("Enter distance "))
        e.append((x,y,d))
    for i in range(n):
        u,v,d=e[i]
        e.append((v,u,d))
    return h,e


def bestfirst(s,t,h,e):
    from queue import PriorityQueue
    closed=[False]*len(h)
    pq=PriorityQueue()
    pq.put((0,s))
    closed[s]=True
    cur=0
    while(pq.empty()==False):
        cur=pq.get()[1]
        print(cur,end=" ")
        if(cur==t):
            break
        for (u,v,c) in e:
            if(u==cur and closed[v]==False):
                closed[v]=True
                pq.put((c,v))
    print()

def aStarAlgo(s, t,e,h):
    open_set = [s]
    closed_set = []
    g = {}             
    parents = {}         
    g[s] = 0
    parents[s] = s
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + h[v] < g[n] + h[n]:
                n = v
        if n == t or haschild(n,e) == False:
            pass
        else:
            for (m, weight) in get_neighbors(n,e):
                if m not in open_set and m not in closed_set:
                    open_set.append(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.append(m)
        if n == None:
            print('Path does not exist!')
            return None
    
        if n == t:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(s)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
    
        open_set.remove(n)
        closed_set.append(n)
    print('Path does not exist!')
    return None

def haschild(n,e):
    for (u,v,t) in e:
        if(u==n):
            return True
    return False


def get_neighbors(v,e):
    res=[]
    for (a,b,c) in e:
        if(a==v):
            res.append((b,c))
    return res


# print("Welcome")
h,e=inputgraph()
s=int(input("Enter source "))
t=int(input("Enter target "))

bestfirst(s,t,h,e)
aStarAlgo(s,t,e,h)