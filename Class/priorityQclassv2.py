class priorityQ():
  
  def __init__(self):
    self.l = []

  def isempty(self):
    return (self.l == [])

  def insert(self,v):
    self.l.append(v)

  def deletemin(self):
    mpos,mval = self.__findmin()
    self.l = self.l[:mpos]+self.l[mpos+1:]
    return mval

  def __findmin(self):
    mpos = 0
    mval = self.l[0]
    for j in range(1,len(self.l)):
      if self.l[j] < mval:
        mval = self.l[j]
        mpos = j
    return (mpos,mval)
 
   
