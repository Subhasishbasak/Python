#Function to find connected components as dictionary
def comp(G):
    j=1
    c={}
    c[j]=list(reachable(G,G.V[0]))
    for i in list(range(1,len(G.V))):
        if G.V[i] not in sum(list(c.values()),[]):
            j=j+1
            c[j]=list(reachable(G,G.V[i]))
    return(c)        


#Function to detect cycle in a graph
def cycl(G):
    ans=0
    for i in list(range(1,len(comp(G))+1)):
        ans=ans+len(comp(G)[i])-1
    if len(sum(G.E,[]))/2 > ans:
        print("The Graph contains Cycle")
    else:
        print("The Graph does not contain Cycle")
        

#Function to detect cycle in a graph using BFS
def cycl_BFS(G):
  nv=set(G.V)  
  for v in G.V:    #In each run of the for loop BFS is performed in a conn comp 
    if v in nv:  
     UnP = {v}
     P = set()
     while (UnP != set()):
       next = UnP.pop()
       for v in G.E[next]:
         if (v in UnP):
             return("The Graph contains Cycle")
         elif not (v in P|UnP):
           UnP.add(v)   
       P.add(next)
     nv=nv-(P|UnP)                
  return("The Graph does not contain Cycle")
        