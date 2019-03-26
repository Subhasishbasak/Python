def selectionsort(l,cmp):
  n = len(l)
  left = 0
  while (left < n - 1):
    cmin = l[left]
    cpos = left
    i = left+1
    while (i < n):
      if cmp(l[i],cmin):
        cmin = l[i]
        cpos = i
      i = i + 1 
    l[left],l[cpos] = l[cpos],l[left]
    left = left + 1
  
MarkList = [("abcd",12),("efgh",12),("ijkl",13),("abc",15),("ef",13)]

def byMarks(x,y):
  nx,mx = x
  ny,my = y
  return mx < my  # changes cpos only if we see value < cmin. Makes it stable

def byName(x,y):
  nx,mx = x
  ny,my = y
  return nx < ny

print(MarkList)
selectionsort(MarkList,byName)
print(MarkList)
selectionsort(MarkList,byMarks)
print(MarkList)

