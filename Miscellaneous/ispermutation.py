def listToDict(l):
  count = {}
  for i in l:
    if i in count:
      count[i] = count[i] + 1
    else:
      count[i] = 1
  return (count)

def ispermutation(l,ls):
   count1 = listToDict(l)
   count2 = listToDict(ls)
   return (count1 == count2)
  
