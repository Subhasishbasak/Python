#All possible topological sort
#from dir_graph import *


def alltopologicalSort(DG):
    count=0
    d={}
    for i in DG.V:
        d[i]=0
    for i in DG.V:
        for j in DG.E[i]:
            d[j]=d[j]+1
    v={}
    for i in DG.V:
        v[i]=0 
    curr=[]    
    def recur(curr,v):
       nonlocal count 
       flag = False  
       for i in DG.V:   
           if d[i]==0 and v[i]==0: 
               for j in DG.E[i]:
                    d[j]=d[j]-1 
               curr.append(i)
               #print(curr)
               v[i]=1 
               recur(curr,v)
               v[i]=0 
               curr.remove(i) 
               for j in DG.E[i]:
                    d[j]=d[j]+1 
               flag = True 
       if not flag: 
          print(curr)
          count=count+1
    recur(curr,v)      
    print("Total number of topological sort : "+ str(count))      

















          
    