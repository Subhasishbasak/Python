def gcdn(a,b):
  m = min(a,b)
  while (m > 0):
    if (a%m == 0) and (b%m == 0):
      return m
    m = m-1
 # If you get here then min(a,b) = 0
  return max(a,b)

def gcdeuc(a,b):
  mn = min(a,b)
  mx = max(a,b)
  if mn == 0:
    return mx
  else:
    #return gcdeuc(mn,mx-mn)
    return gcdeuc(mn,mx%mn)

def gcdeucNoRec(a,b):
  mn = min(a,b)
  mx = max(a,b)
  while (mn > 0):
    mn,mx = min(mn,mx%mn),max(mn,mx%mn)
  return(mx)

