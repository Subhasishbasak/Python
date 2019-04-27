class OpenHash:

  def __init__(self,m=16):
    self.length = m
    self.Table = []  # 2 element lists. [Deleted?, (key,value)]
    for i in range(0,m):
      self.Table.append([False,None])

  def __myH(self,key,i):
    return((hash(key)%self.length)^i)


  def search(self,key):
    for i in range(0,self.length):
      nextpos = self.__myH(key,i)
      if self.Table[nextpos][1] == None:
        return None 
      x,y = self.Table[nextpos][1]
      if not self.Table[nextpos][0] and x == key:
        return y
    return None

  def insert(self,key,value):
    pos = -1
    for i in range(0,self.length):
      nextpos = self.__myH(key,i)
      if self.Table[nextpos][1] == None: # key not found
        if pos < 0:
          pos = nextpos
        self.Table[pos][0] = False
        self.Table[pos][1] = (key,value)
        return
      if self.Table[nextpos][0] and pos < 0:
        pos = nextpos
      elif not self.Table[nextpos][0]:
        x,y = self.Table[nextpos][1]
        if x == key:
          self.Table[nextpos][1] = (key,value)
          return
     
  def delete(self,key):
    for i in range(0,self.length):
      nextpos = self.__myH(key,i)
      if self.Table[nextpos][1] == None:
        return 
      x,y = self.Table[nextpos][1]
      if not self.Table[nextpos][0] and x == key:
        self.Table[nextpos][0] = True

  def __str__(self):
    ans = ""
    for i in range(0,self.length):
      ans = ans + str(self.Table[i])
    return ans
      
    

