# Assumes the Universe is 1 .. 10^6
import random as R
class hashtable():
  
   def __init__(self,m = 100):
     self.length = m
     self.Table = []  
     self.p = 1000003
     for i in range(0,self.length):
       self.Table.append([])
     self.a = R.randint(1,self.p-1)
   
   def insert(self,key,value):
     bucket = ((self.a * key) % self.p) % self.length
     for i in range(0,len(self.Table[bucket])):
       x,y = self.Table[bucket][i]
       if x == key:
         self.Table[bucket][i] = (key,value)
     else:
       self.Table[bucket].append((key,value)) 
        

   def search(self,key):
     bucket = ((self.a * key) % self.p) % self.length
     for i in range(0,len(self.Table[bucket])):
       x,y = self.Table[bucket][i]
       if x == key:
         return(y)
     return None


   def delete(self,key): 
     bucket = ((self.a * key) % self.p) % self.length
     found = False
     for i in range(0,len(self.Table[bucket])):
       x,y = self.Table[bucket][i]
       if x == key:
         self.Table[bucket].pop(i)
         return
     
   def __str__(self):
     x = []
     for i in self.Table:
       x.append(str(i))
     return str(x)
       

