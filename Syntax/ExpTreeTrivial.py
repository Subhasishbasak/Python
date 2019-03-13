from Tree import *

class ExpTree(Tree):

   def evaluate(self):
     if self.isempty():
       return None
     if self.leaf():
       return self.value
     if self.value == '+':
       return(self.left.evaluate() + self.right.evaluate())
     elif self.value == '-':
       return(self.left.evaluate() - self.right.evaluate())
     elif self.value == '*':
       return(self.left.evaluate() * self.right.evaluate())
     return None

   def __str__(self):
      #return Tree.__str__(self)+","+Tree.__str__(self)
      return super().__str__()+","+super().__str__()
