def deletemin(l): # assumes l is not empty
  #ls = []
  #for i in list(range(0,len(l))):
  #  ls.append((l[i],i))
  ls = list(zip(l,list(range(0,len(l)))))
  cmin,pos = min(ls)
  return (cmin,l[:pos]+l[pos+1:])

def selectionsort(l):
  ans = []
  while (l != []): 
    v,ls = deletemin(l)
    ans.append(v)
    l = ls
  return(ans)
