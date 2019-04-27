#Bloom filter using Multiplicative hashing

import random as R
class BloomFilter():
    def __init__(self,m,k):
        self.length=m
        self.Table=[]
        for i in range(0,self.length):
            self.Table.append([0])  
        self.a = R.sample(range(1,10),k)

            
    def insert(self,v):
        h1=(self.a[0] * v)% self.length
        h2=(self.a[1] * v)% self.length
        h3=(self.a[2] * v)% self.length
        for i in range(1,4):
            self.Table[h1]=1
            self.Table[h2]=1
            self.Table[h3]=1  
        
    def isthere(self,v):
        h1=(self.a[0] * v)% self.length
        h2=(self.a[1] * v)% self.length
        h3=(self.a[2] * v)% self.length        
        if self.Table[h1]==1 and self.Table[h2]==1 and self.Table[h3]==1:
            print("Yes")
        else:
            print("No")
            
    
    def __str__(self):
        x = []
        for i in self.Table:
           x.append(str(i))
        return str(x)
    
    
    
class BloomFilter2():
    def __init__(self,m,k):       # k: no. of hash functions
        self.length=m
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
      