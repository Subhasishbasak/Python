def quicksort(l):
  if len(l) < 1:
    return l
  p = l[0]
  leftlist = []
  rightlist = []
  for i in l[1:]:
    if i < p :
      leftlist.append(i)
    else:
      rightlist.append(i)
  return(quicksort(leftlist) + [p] + quicksort(rightlist))
 
