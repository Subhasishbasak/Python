#DAG
#from dir_graph import *

def indeg(DG,v):
    d={}
    for i in DG.V:
        d[i]=0
    for i in DG.V:
        for j in DG.E[i]:
            d[j]=d[j]+1
    return (d[v])        


#DAG => topological sortig exists
#i.e. If there is no topological sorting, the directed graph contains cycle     

def dir_cycl(DG):
    d={}
    for i in DG.V:
        d[i]=0
    for i in DG.V:
        for j in DG.E[i]:
            d[j]=d[j]+1     #computes the indegrees
    ans=[]
    q=[]
    for v in DG.V:
      if d[v]==0:
          q.append(v)
    while(q!=[]):
        next=q.pop(0)
        ans.append(next)
        for i in DG.E[next]:
            d[i]=d[i]-1
            if d[i]==0:
                q.append(i)
    if len(ans)!=len(DG.V):
       return("The directed graph contains cycle")
    else:
       return("The topological sorted list is : "+str(ans))
                


n = 9
l = [(1,4),(4,5),(2,3),(6,7),(7,9),(9,8),(1,9)]
DG=dir_graph(n,l)
dir_cycl(DG)            
            
          