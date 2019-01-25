#Directed Graph

class dir_graph():
    
    def __init__(self,n,l):
        self.V=list(range(1,n+1))
        self.E=[[]]
        for v in self.V :
           self.E.append([]) 
        for e in l:
           u,v = e
           self.E[u].append(v)
           
    def view(self):
        for i in self.V :
           print(i,self.E[i])    

n = 9
l = [(1,4),(4,5),(2,3),(6,7),(7,9),(9,8),(1,9)]
#G = Graph(n,l)
DG=dir_graph(n,l)
#G.view()
DG.view()