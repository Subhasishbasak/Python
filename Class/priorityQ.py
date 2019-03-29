l = []

def isempty():
  return (l == [])

def insert(v):
  l.append(v)

def deletemin():
  global l
  mpos = 0
  mval = l[0]
  for j in range(1,len(l)):
    if l[j] < mval:
      mval = l[j]
      mpos = j
  l = l[:mpos]+l[mpos+1:]
  return mval
   
