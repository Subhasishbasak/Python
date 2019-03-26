def insert(v,l): 
  cpos = 0
  while cpos < len(l) and l[cpos] < v : 
     cpos = cpos + 1
  return l[:cpos] + [v] + l[cpos:]


def insertionsort(l):
  ans = []
  while l :
    v = l.pop()
    ans = insert(v, ans)
  return(ans)
