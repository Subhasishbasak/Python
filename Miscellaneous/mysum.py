def mysum(l):
  sum = 0
  for i in l:
    sum = sum + i
  return(sum)

def mysumrec(l):
  if l == [] :
    return 0
  else :
    return l[0] + mysumrec(l[1:])

''' if l == []:
    return(0)
  else:
    return l[-1] + mysumrec(l.pop()) '''



