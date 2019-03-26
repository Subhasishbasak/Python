def quicksort(l,b,e): 
  if e-b < 1:
    return
  p = l[b]
  left = b+1
  right = b+1
  ''' Invariant:
      left <= right
      if b <= i < left then l[i] <= p
      if left <= i < right then l[i] > p '''
  # Invariant is established here.
  while (right <= e):
    if (l[right] > p):
      right = right + 1
    else:
      l[left],l[right] = l[right],l[left]
      left = left + 1
      right = right + 1
  #The body of the loop preserves the invariant
  if left > b+1 :
    l[b],l[left-1] = l[left-1],l[b]
    quicksort(l,b,left-2)
    quicksort(l,left,e)
  else:
    quicksort(l,b+1,e)
  return l  


   
  
