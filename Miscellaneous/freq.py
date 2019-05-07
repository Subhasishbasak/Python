def freq(l):
  ans = []
  if l == []:
    return []
  curr = l[0]
  count = 1
  i = 1
  while i < len(l):
    if l[i] == curr:
      count = count + 1
    else:
      ans.append((curr,count))
      curr = l[i]
      count = 1
    i = i+1
  ans.append((curr,count)) 
  return(ans)
    
# Freq using sets

def count(v,l):
  ans = 0
  for i in l:
    if v == i:
      ans = ans + 1
  return ans

# Works even if the list is not sorted
def freqSet(l):
  s = set(l)
  ans = []
  for v in s:
    ans.append((v,count(v,l)))
  return(ans)

# Freq using dictionaries --- works on lists that are not sorted

def freqDict(l):
  count = {}
  for i in l:
    if i in count:
      count[i] = count[i] + 1
    else:
      count[i] = 1
  return(list(count.items()))
  
