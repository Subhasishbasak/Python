from priorityQheap import *

def heapsort(l):
  x = priorityQ()
  for i in l:
    x.insert(i)
  ans = []
  while not x.isempty():
    ans.append(x.deletemin())
  return(ans)
