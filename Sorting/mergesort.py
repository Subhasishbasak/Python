def merge(l1,l2): # assume l1 and l2 are sorted 
  if l1 == [] or l2 == []:
    return l1 + l2
  if l1[0] <= l2[0]:
    return [l1[0]] + merge(l1[1:], l2)
  else:
    return [l2[0]] + merge(l1, l2[1:])

def mergeIter(l1,l2):
  ans = []
  while (l1 != [] and l2 != []):
    if l1[0] <= l2[0]:
      ans.append(l1[0])
      l1.pop(0)
    else:
      ans.append(l2[0])
      l2.pop(0)
  ans = ans + l1 + l2
  return ans

def mergesort(l):
  if len(l) < 2:
    return l
  mid = len(l)//2
  leftlist = l[0:mid]
  rightlist = l[mid:]
  return merge(mergesort(leftlist),mergesort(rightlist))

 

  
  


    


