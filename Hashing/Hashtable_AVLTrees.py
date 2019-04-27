#Chaining in Hashtable with AVL Trees_tuple

from HTree import *


def cmp(a,b):
      x,y=a
      p,q=b
      if x<p:
          return True
      else:
          return False
  
  def equal(a,b):
      x,y=a
      p,q=b
      if x==p:
          return True
      else:
          return False
      
class AVLTree_tupl(HTree):
  
  def search(self, v):
    if self.isempty():
      return False
    if equal(self.value,v):
      return True
    if cmp(self.value,v):
      return self.right.search(v)
    else:
      return self.left.search(v)

  def insert(self,v):
    if self.isempty():
      self.value = v
      self.left = AVLTree()
      self.right = AVLTree()
      self.height = 1
    if equal(self.value,v):
       return 
    if cmp(self.value,v):
       self.right.insert(v)
    else:
      self.left.insert(v)
    self.fixheight()
    self.rebalance()
    return

  def deletemax(self):
    if self.isempty():
      return None
    if self.right.isempty(): # This node is the maximum
      v = self.value
      tmp = self.left
      self.value, self.left,self.right = tmp.value,tmp.left,tmp.right
      self.height = tmp.height
      # The two lines below are not needed for correctness
      tmp.value, tmp.left,tmp.right = None,None,None
      tmp = None
      self.rebalance()
      return v
    else:
      v = self.right.deletemax()
      self.fixheight()
      self.rebalance()
      return(v)

  def delete(self,v):
    if self.isempty():
      return
    if cmp(self.value,v):
      self.right.delete(v)
      self.fixheight()
    elif not cmp(self.value,v) and not equal(self.value,v):
      self.left.delete(v)
      self.fixheight()
    else: # v sits in the current node
      if self.left.isempty():
        tmp = self.right
        self.left,self.right = tmp.left,tmp.right
        self.value,self.height = tmp.value,tmp.height
        # Next lines not needed for correctness
        tmp.value,tmp.left,tmp.right,tmp.height = None, None, None, None
        tmp = None
      else:
        self.value = self.left.deletemax()
        self.fixheight()
    self.rebalance()

#Hash table with AVL Trees
class hashtable():
  
   def __init__(self,m):
     self.length = m
     self.Table = []  
     for i in range(0,self.length):
       self.Table.append(AVLTree_tupl())
   
   def insert(self,key,value):
     hkey = hash(key)
     bucket = hkey % self.length
     if self.Table[bucket].search((key,value)):
         self.Table[bucket].delete((key,value))
         self.Table[bucket].insert((key,value)) 
     else:
        self.Table[bucket].insert((key,value)) 
        

   def search(self,key):
     hkey = hash(key)
     bucket = hkey % self.length
     if not self.Table[bucket].isempty():
         return True
     else:
         return False 


   def delete(self,key,value): 
     hkey = hash(key)
     bucket = hkey % self.length
     if self.Table[bucket].search((key,value)):
         self.Table[bucket].delete((key,value))
     else:
         return("Not found")

     
   def __str__(self):
     x = []
     for i in self.Table:
       x.append(str(i))
     return str(x)