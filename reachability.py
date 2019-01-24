from Graph import *

# find all the vertices reachable from a given vertex
def reachable(G,v):
  UnP = {v}
  P = set()
  while (UnP != set()):
    next = UnP.pop()
    for v in G.E[next]:
      if not (v in P|UnP):
        UnP.add(v)
    P.add(next)
  return(P)

def depthFS(G,s):
   offset = 0 
   reach = set()
   def dfs(v):
    nonlocal G,reach,offset
    offset = offset + 1
    print(" "*offset +"Entering "+str(v))
    reach.add(v)
    for u in G.E[v]:
      if not (u in reach):
        dfs(u)
    print(" "*offset + "Leaving "+str(v))
    offset = offset - 1
   dfs(s)
   return(reach)
    
def breadthFS(G,s):
    distance = {}
    for v in G.V:
     distance[v] = -1
    queue = [s]
    distance[s] = 0
    while (queue != []):
      next = queue.pop(0)
      for u in G.E[next]:
        if distance[u] == -1:
           queue.append(u)
           distance[u] = distance[next] + 1
    return(distance) 
     

n = 9
l = [(1,4),(4,5),(5,1),(2,3),(6,7),(7,9),(9,8)]
G = Graph(n,l)
print(G.E)
#print(reachable(G,6))
print(breadthFS(G,1).items())

n = 8
l = [(1,2),(2,3),(2,5),(3,4),(1,6),(6,8),(6,7),(8,7)]
G = Graph(n,l)
#print(depthFS(G,1))
print(breadthFS(G,1).items())


