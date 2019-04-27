# A trivial Hashtable

class hashtable():
  
   def __init__(self,m = 10):
     self.length = m
     self.Table = []  
     for i in range(0,self.length):
       self.Table.append([])
   
   def insert(self,key,value):
     hkey = hash(key)
     bucket = hkey % self.length
     for i in range(0,len(self.Table[bucket])):
       x,y = self.Table[bucket][i]
       if x == key:
         self.Table[bucket][i] = (key,value)
     else:
       self.Table[bucket].append((key,value)) 
        

   def search(self,key):
     hkey = hash(key)
     bucket = hkey % self.length
     for i in range(0,len(self.Table[bucket])):
       x,y = self.Table[bucket][i]
       if x == key:
         return(y)
     return None


   def delete(self,key): 
     hkey = hash(key)
     bucket = hkey % self.length
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
       

