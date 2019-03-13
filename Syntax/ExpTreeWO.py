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

'''   def __str__(self):
     if self.isempty():
       return("")
     if self.leaf():
       return(str(self.value))
     return("("+str(self.left)+str(self.value)+str(self.right)+")")
'''
