def binarysearch(v,l):
  left = 0
  right = len(l) - 1
  while left <= right :
    mid = (left + right)//2
    if l[mid] == v:
      return True
    elif l[mid] < v:
      left = mid + 1
    else: 
      right = mid - 1
  return False

def search(v,l):
  for i in l:
    if v == i:
      return True
  return False
