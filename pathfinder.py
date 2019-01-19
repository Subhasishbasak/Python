#BFS with pathfinder
#from Graph import *


def pathfinder(G,s,e):
    distance = {}
    parent={}
    for v in G.V:
     distance[v] = -1
    queue = [s]
    distance[s] = 0
    parent[s]=0
    while (queue != []):
      next = queue.pop(0)
      for u in G.E[next]:
        if distance[u] == -1:
           queue.append(u)
           distance[u] = distance[next] + 1
           parent[u]=next      
    if e not in list(parent.keys()):
        return ("Not reachable")
    else:
        ans=[e]
        prev=parent[e]
        while prev!=s:
            ans.append(prev)
            prev=parent[prev]
        ans.append(s)    
    return (ans,distance[e])        
            
            
n = 10
l = [(1,2),(1,3),(2,3),(1,8),(4,5),(4,8),(5,7),(5,6),(6,7),(6,9),(6,8),(8,9),(9,10)]
G = Graph(n,l)            
    
    
