def palin(l):
  ans = True
  n = len(l)
  for i in range(0,n//2):
    if (l[i] != l[n-i-1]) :
      ans = False
      break
  return(ans)


def palinrec(l):
   if l == []:
     return True
   elif l[0] != l[-1]: 
     return False
   else: 
     return palinrec(l[1:len(l)-1])

ls = [2,3,4,2,3]

palin(ls)
