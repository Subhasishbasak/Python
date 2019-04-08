''' Our algorithm does the following:
    search(v,l,i,j): 
      mid = i+j//2 
      if l[mid] == v return True
      if l[mid] > v then search(v,l,i,mid-1)
                    else search(v,l,mid+1,j) '''

def binarysearch(v,l): # assumes that l is sorted
  def bsearch(i,j): 
    if i > j:
      return False
    if i == j:
      return l[i] == v
    mid = (i+j)//2
    if l[mid] == v:
      return True
    if l[mid] > v:
      return bsearch(i,mid-1)
    else:
      return bsearch(mid+1,j)
  return bsearch(0,len(l)-1)

