# Find the shortest path to reachable positions in a grid 
# from 0,0. You can only move to a potential neighbour (up,down,left,right)
# if the difference is <= k. g is a list of lists representing a square grid.

def reach(g,k):


   N = len(g)
   shortest = {}
   for i in range(0,N):
     for j in range(0,N):
      shortest[i,j] = -1
   shortest[0,0] = 0
   queue = [(0,0)]
   while (queue != []):
     (a,b) = queue.pop(0)
     neigh = []
     if (a > 0) and abs(g[a][b] - g[a-1][b]) <= k :
       neigh.append((a-1,b))
     if (b > 0) and abs(g[a][b] - g[a][b-1]) <= k :
       neigh.append((a,b-1))
     if (a < N-1) and abs(g[a][b] - g[a+1][b]) <= k:
       neigh.append((a+1,b))
     if (b < N-1) and abs(g[a][b] - g[a][b+1]) <= k:
       neigh.append((a,b+1))
     for next in neigh:
       if shortest[next] == -1 :
         queue.append(next)
         shortest[next] = shortest[a,b] + 1
    
   for i in range(0,N):
     for j in range(0,N):
       print(shortest[i,j],end=" ")
     print(" ")

     
     
g = [[3,1,8,4,6],[2,9,3,2,4],[4,1,8,6,2],[4,4,3,2,1],[6,3,3,2,4]]

reach(g,3)

    

