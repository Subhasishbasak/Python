#Practice problem 4
#Q.1

#fixing the no. of hash functions to 1

class BloomFilter():
    def __init__(self,m):       
        self.length=m*8
        self.table=[]
        self.h=0  
        for i in range(0,self.length):
            self.table.append([0])
        self.a = R.randint(1,10)  
            
    def insert(self,v):
            self.h=(self.a * hash(v))% self.length
            self.table[self.h]=1

    def isthere(self,v):
            self.h=(self.a * hash(v))% self.length
            if self.table[self.h]!=1:
                return False
            return True
            
    def __str__(self):
        x = []
        for i in self.table:
           x.append(str(i))
        return str(x)
  
                 
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



#Q.2


'''
state 0: outside not willing to take
state 1: outside willing to take
state 2: inside a potential firstword

state 0:
    "." not followed by integer => state 1
    everything else => state 0
state 1:
    everything except whitespace => state 2, store
    whitespace => state 1
state 2:
    whitespace => append to ans, state 0
    everything else => state 2, store
'''      
def firstwords(l):
    State=1
    curr=[]
    ans=[]
    for i in list(range(0,len(l))):
        if State==0:
            if(l[i] == ".") and (i < len(l)-1) and not(l[i+1].isdigit()):
                State=1
        elif State==1:
            if l[i]!=" ":
                State=2
                curr.append(l[i])    
        elif State==2:
            if l[i]==" ":
                State=0
                ans.append("".join(curr))
                curr=[]
            else:
                curr.append(l[i])
        print(curr,State)                    
    return ans         
        

#Q.3

p1=re.compile(r'-')
p2=re.compile(r'[G-Zg-z]')
p3=re.compile(r'\D*(\d+)\D*')

def func(l):
    for i in l:
        if int(i)<0 or int(i)>255:
            return False
    return True    


import re
p=re.compile(r'host\s+(\w+)\s+{\s+hardware\s+ethernet\s+(\w\w[:-]+\w\w[:-]+\w\w[:-]+\w\w[:-]+\w\w[:-]+\w\w);\s+fixed-address\s+(\d+.\d+.\d+.\d+);}')
with open("dhcp.txt","r") as f:
  ls = f.read()
  m = p.findall(ls)
  for x in m:
    if p2.findall(x[1])==[] and func(p3.findall(x[2])):
       print(x[0]+","+(p1.sub(r':',x[1])).upper()+","+x[2])
    else:
       print(x[0]+","+(p1.sub(r':',x[1])).upper()+","+x[2]+" "+"Error") 


#Q.4
    
def article(l):
    p1=re.compile(r'\W(a)\s+(?=[aeiou])')
    p2=re.compile(r'\W(an)\s+(?![aeiou])')
    p3=re.compile(r'\W*(A)\s+(?=[aeiou])')
    p4=re.compile(r'\W*(An)\s+(?![aeiou])')
    return(p2.sub(r" a ",p1.sub(r" an ",p3.sub(r"An ",p4.sub(r"A ",l)))))


#p=re.compile(r'host\s+(\w+)\s+{\s+hardware\s+ethernet\s+(\w\w[:-]){4}\w\w);\s+fixed-address\s+(\d+.\d+.\d+.\d+);}')

  
#Q.5
    
    
def allbst(n):
    def constructTrees(s,e): 
        curr=[]
        if s>e:
           return [AVLTree()]
        elif s==e:
           return [AVLTree(s)]
        else:
           for i in list(range(s,e+1)):
               leftSubtree  = constructTrees(s,i-1)
               rightSubtree = constructTrees(i+1,e)
               for j in leftSubtree:  
                   for k in rightSubtree: 
                       curr.append(AVLTree(i,AVLTree(j),AVLTree(k)))
        return curr 
    for i in constructTrees(1,n):
        print(str(i))    #prints with height  
    
           

    
       

