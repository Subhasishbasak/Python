class priorityQ():
  
  def __init__(self):
    self.l = []
    self.length = 0

  def isempty(self):
    return (self.length == 0)

  def insert(self,v):
    self.l.append(v)
    self.length = self.length + 1
    curr = self.length - 1
    while (curr > 0) and (self.l[curr] < self.l[(curr-1)//2]):
      self.l[curr],self.l[(curr-1)//2] = self.l[(curr-1)//2],self.l[curr]
      curr = (curr-1)//2

  def deletemin(self):
    self.l[0],self.l[self.length-1] = self.l[self.length-1],self.l[0] 
    self.length = self.length-1
    curr = 0
    while (2*curr+1 < self.length):
      left = 2*curr + 1
      right = 2*curr + 2
      next = curr
      if self.l[left] < self.l[curr]:
        self.l[left],self.l[curr] = self.l[curr],self.l[left]
        next = left
      if (right < self.length) and (self.l[right] < self.l[curr]):
        self.l[right],self.l[curr] = self.l[curr],self.l[right]
        next = right
      if next == curr:
        break
      else:
        curr = next
    return(self.l.pop())

