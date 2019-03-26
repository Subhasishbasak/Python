def deletemin(l): # assumes l is not empty
  cmin = l[0]
  cpos = 0
  for i in range(0,len(l)):
    if l[i] < cmin:
      cmin = l[i]
      cpos = i
  return (cmin,l[:cpos]+l[cpos+1:])

def selectionsort(l):
  ans = []
  while (l != []): 
    v,ls = deletemin(l)
    ans.append(v)
    l = ls
  return(ans)
