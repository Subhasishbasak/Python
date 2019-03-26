def selectionsort(l):
  n = len(l)
  left = 0
  while (left < n - 1):
    cmin = l[left]
    cpos = left
    i = left+1
    while (i < n):
      if l[i] < cmin:
        cmin = l[i]
        cpos = i
      i = i + 1 
    l[left],l[cpos] = l[cpos],l[left]
    left = left + 1
    print(left,l)
  
