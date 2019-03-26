def mergesort(l,cmp):

  def merge(l1,l2): # assume l1 and l2 are sorted 
    if l1 == [] or l2 == []:
      return l1 + l2
    if cmp(l1[0],l2[0]):
      return [l1[0]] + merge(l1[1:], l2)
    else:
      return [l2[0]] + merge(l1, l2[1:])

  if len(l) < 2:
    return l
  mid = len(l)//2
  leftlist = l[0:mid]
  rightlist = l[mid:]
  return merge(mergesort(leftlist,cmp),mergesort(rightlist,cmp))

MarkList = [("abcd",12),("efgh",14),("efg",21),("ijkl",14)]
 
def byMarks(x,y):
  nx,mx = x
  ny,my = y
  return mx <= my

def byName(x,y):
  nx,mx = x
  ny,my = y
  return nx <= ny

print(MarkList)
print(mergesort(MarkList,byMarks))
print(mergesort(MarkList,byName))
