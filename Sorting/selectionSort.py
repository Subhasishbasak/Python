def deletemin(l): # assumes l has length i
  cmin = l[0]            # one step
  cpos = 0               # one step
  for i in range(0,len(l)): # totally i iterations taking 3 * i steps
    if l[i] < cmin:      # one step
      cmin = l[i]        # one step
      cpos = i           # one step
  return (cmin,l[:cpos]+l[cpos+1:])  # i steps here as list has to copied

# over all on input of length i, deletemin takes: 2 + 3*i + i = 4i + 2

def selectionsort(l):     # Input list of size N
  ans = []                # one unit of time
  while (l != []):        # executed N times with lists of size N,N-1,N-2 ...i 
    v,ls = deletemin(l)
    ans.append(v)         # takes one unit of time
    l = ls                # one unit of time
  return(ans)

# cost of selection sort on input of length N 
# 1 + (1 + (4N+2) + 2) + (1 + (4(N-1)+2) + 2) + (1 + (4(N-2)+2) + 2) ... (1 + 4.1 + 2)
# =  1 + (5 + 4N) + (5 + 4(N-1)) + (5 + 4(N-2)) ...  + (5 + 4.1)
# =  1 + 5N + 4(N(N+1)/2)
# =  O(N^2)
