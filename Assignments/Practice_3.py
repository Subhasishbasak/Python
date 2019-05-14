#Practice problem 3
#Q.1

#from AVLTree import *

#Q.1  (returns the largest value smaller than v)
def leftval(x,v):
    if x.isempty():
        print(None)
        return
    if x.value==v:
        if x.left.isempty():
            print(None)
            return
        else:
            return x.left.deletemax()
    elif x.value>v:
        if x.left.isempty():
            print(None)
            return 
        else:
            return leftval(x.left,v)
    else:
        if x.right.isempty():
            return x.value
        elif x.right.value>=v:
            return x.value
        else:
            return leftval(x.right,v)
    
''' 
 def deletemin(self):
    if self.isempty():
      return None
    if self.left.isempty(): # This node is the maximum
      v = self.value
      tmp = self.right
      self.value, self.right,self.left = tmp.value,tmp.right,tmp.left
      self.height = tmp.height
      # The two lines below are not needed for correctness
      tmp.value, tmp.right,tmp.left = None,None,None
      tmp = None
      self.rebalance()
      return v
    else:
      v = self.left.deletemin()
      self.fixheight()
      self.rebalance()
      return(v)  
'''    
#(returns the smallest value larger than v)   
def rightval(x,v):
     if x.isempty():
         print(None)
         return
     if x.value==v:
         if x.right.isempty():
            print(None)
            return
         else:
            return x.right.deletemin() #define deletemin() in AVLTree
     elif x.value<v:
         if x.right.isempty():
            print(None)
            return 
         else:
            return rightval(x.right,v)
     else:
         if x.left.isempty():
             return x.value
         elif x.left.value<=v:
             return x.value
         else:
             return rightval(x.left,v)   

#Q.2

def lcaVal(x,u,v):
     ans=x.value
     df_1=ans-u
     df_2=ans-v
     df=df_1*df_2
     while(df>0):
         if df_1>0:
             return lcaVal(x.left,u,v)
         else:
             return lcaVal(x.right,u,v)
     return ans    
                 
#Q.3
#from HTree import *

class AVLTree(HTree):
      
  opcount=0 
   
  def search(self, v):
    if self.isempty():
      self.opcount=self.opcount+1  
      return False
    if self.value == v:
      self.opcount=self.opcount+1
      return True
    if self.value < v:
      self.opcount=self.opcount+1
      return self.right.search(v)
    else:
      self.opcount=self.opcount+1  
      return self.left.search(v)

  def insert(self,v):
    if self.isempty():
      self.opcount=self.opcount+1  
      self.value = v
      self.left = AVLTree()
      self.right = AVLTree()
      self.height = 1
      return
    if self.value == v:
      self.opcount=self.opcount+1  
      return 
    if self.value < v:
      self.opcount=self.opcount+1  
      self.right.insert(v)
    else:
      self.opcount=self.opcount+1  
      self.left.insert(v)
    self.fixheight()
    self.rebalance()
    return

  def deletemax(self):
    if self.isempty():
      self.opcount=self.opcount+1  
      return None
    if self.right.isempty(): # This node is the maximum
      self.opcount=self.opcount+1
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
      self.opcount=self.opcount+1  
      v = self.right.deletemax()
      self.fixheight()
      self.rebalance()
      return(v)

  def delete(self,v):
    if self.isempty():
      self.opcount=self.opcount+1  
      return
    if self.value < v:
      self.opcount=self.opcount+1  
      self.right.delete(v)
      self.fixheight()
    elif self.value > v:
      self.opcount=self.opcount+1  
      self.left.delete(v)
      self.fixheight()
    else: # v sits in the current node
      if self.left.isempty():
        self.opcount=self.opcount+1  
        tmp = self.right
        self.left,self.right = tmp.left,tmp.right
        self.value,self.height = tmp.value,tmp.height
        # Next lines not needed for correctness
        tmp.value,tmp.left,tmp.right,tmp.height = None, None, None, None
        tmp = None
      else:
        self.opcount=self.opcount+1  
        self.value = self.left.deletemax()
        self.fixheight()
    self.rebalance()
    
  def report(self):
      if self.isempty():  
          return 0
      else:
          return(self.opcount+self.left.report()+self.right.report())

#Q.4
import random as R      
class hashtable():
    
   opCount=0
   def __init__(self,m = 5000):
     self.length = m
     self.Table = []  
     self.p = 5001
     for i in range(0,self.length):
       self.Table.append([])
     self.a = R.randint(1,self.p-1)
   
   def insert(self,key,value):
     bucket = ((self.a * key) % self.p) % self.length
     found=False
     for i in range(0,len(self.Table[bucket])):
       x,y = self.Table[bucket][i]
       self.opCount=self.opCount+1
       if x == key:
         self.Table[bucket][i] = (key,value)
         found=True
     if not found:
       self.Table[bucket].append((key,value)) 
       self.opCount=self.opCount+1 

   def search(self,key):
     bucket = ((self.a * key) % self.p) % self.length
     for i in range(0,len(self.Table[bucket])):
       x,y = self.Table[bucket][i]
       self.opCount=self.opCount+1
       if x == key:
         return(y)
     return ("Not found")


   def delete(self,key): 
     bucket = ((self.a * key) % self.p) % self.length
     found = False
     for i in range(0,len(self.Table[bucket])):
       x,y = self.Table[bucket][i]
       self.opCount=self.opCount+1
       if x == key:
         self.Table[bucket].pop(i)
         found=True
     if not found:
         return("Value not found")
     
   def __str__(self):
     x = []
     for i in self.Table:
       x.append(str(i))
     return str(x)
     
   def report(self):
      print(self.opCount)          

#Q.5

import random as R
l=[]
while (len(l)<3000):
    a=R.randint(1,5000)
    if a not in l:
        l.append(a)
x=hashtable()        
for i in l: 
  x.insert(i,"i") 
x.report() #around 4k 
  
l=[]
while (len(l)<3000):
    a=R.randint(1,5000)
    if a not in l:
        l.append(a)
x=AVLTree()        
for i in l: 
  x.insert(i) 
x.report() #around 33k    



#Q.7
class BloomFilter():
    def __init__(self,m,k):       # k: no. of hash functions
        self.length=m*8
        self.table=[]
        self.h=[]  
        for i in range(0,self.length):
            self.table.append([0])
        self.a = R.sample(range(1,10),k)  
        for i in range(0,k):
            self.h.append([])
            
    def insert(self,v):
        for i in range(0,k):
            self.h[i]=(self.a[i] * hash(v))% self.length
            self.table[self.h[i]]=1

    def isthere(self,v):
        for i in range(0,k):
            self.h[i]=(self.a[i] * hash(v))% self.length
            if self.table[self.h[i]]!=1:
                return False
        return True
            
    def __str__(self):
        x = []
        for i in self.table:
           x.append(str(i))
        return str(x)
  
import re
                 
def wordsearch(a,b):
    ans=[]
    with open(a,"r") as f:
       ip=f.read()
    with open(b,"r") as f:
       w=f.read()
    p = re.compile(r'\S+')
    ip=p.findall(ip)   
    w=p.findall(w)
    x=BloomFilter(len(ip),5)
    for i in ip:
       x.insert(i)
    for i in w:
        if x.isthere(i) and i not in ip:
            ans.append(i)
    return (ans)        



        
            
  
       
    



        
             