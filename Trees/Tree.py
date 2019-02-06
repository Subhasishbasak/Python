class Tree():

  def  __init__(self,v=None,l=None,r=None):
    if v == None:
      self.value = None
      self.left = None
      self.right = None
    else:
      if l == None:
        l = Tree()
      if r == None:
        r = Tree()
      self.left = l
      self.right = r
      self.value = v

  def isempty(self):
    if self.value == None:
      return True
    return False

  def __str__(self):
    if self.isempty():
       return ("E")
    return("( "+str(self.value)+" "+str(self.left)+" "+str(self.right)+" )")
   
  def inorder(self):
    if self.isempty():
      return([])
    return(self.left.inorder() + [self.value] + self.right.inorder())

  def postorder(self):
    if self.isempty():
      return([])
    return(self.left.postorder()+self.right.postorder() + [self.value])
       
  def leaf(self):
    if self.isempty():
      return False
    if (self.left.isempty() and self.right.isempty()):
      return True
    return False

  def ht(self):
    if self.isempty():
      return 0
    return 1+max(self.left.ht(), self.right.ht())
