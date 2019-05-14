#Practice problem 1
#Q.1

def hexa(v):
    ans=0
    d={}
    d["A"],d["B"],d["C"],d["D"],d["E"],d["F"]=[10,11,12,13,14,15]
    for i in list(range(0,len(v))):
        if v[i] in ["A","B","C","D","E","F"]:
            ans=ans+d[v[i]]*16**(len(v)-1-i)
        else:
            ans=ans+int(v[i])*16**(len(v)-1-i)
    print(ans)  

hexa("1A")      
            
#Q.2
def bleft(v,l):
   def binarysearch(v,l):
       a=0
       b=len(l)-1
       while(a<=b):
           mid=(a+b)//2
           if v==l[mid]:
               return (True,mid)
           elif v>l[mid]:
               a=mid+1
           else:
               b=mid-1
       return (False,b)
   m,n=binarysearch(v,l)
   if m==True:
       pos=n-1
       while l[pos]==v:
           pos=pos-1
       return pos
   else:
       if n>0:
           return n
       else:
           return -1
    
bleft(7,[4,5,6,6,6,7])

#Q.3
def quickcount(v,l):
    count=0
    n=bleft(v,l)
    pos=n+1
    while pos<len(l) and l[pos]==v:
       pos=pos+1
       count=count+1
    return count       
        
quickcount(3,[3,3,3,3,4,5])

#Q.4
def validrow(l):
    s=set([1,2,3,4,5,6,7,8,9])
    if s==set(l) and len(l)==9:
        return True
    else:
        return False

validrow([1,2,3,7,5,6,4,8,9])    

def transpose(l):
    t=[]
    for i in list(range(0,len(l))):
        t.append(list(range(0,len(l))))
    for i in list(range(0,len(l))):
        for j in list(range(0,len(l))):
            t[j][i]=l[i][j]
    return t        

def blocksTorows(l):
    ans=[]
    for i in range(0,3):
        ans.append(list(range(0,9)))
    for i in list(range(0,3)):      
       ans[i]=l[0][3*i:3+3*i]+l[1][3*i:3+3*i]+l[2][3*i:3+3*i]
    return ans
            
def validsolution(l):
    for i in list(range(0,9)):
        if not validrow(l[i]):
            print("Not a valid solution")  #checks whether a row is valid
            break
        if not validrow(transpose(l)[i]):
            print("Not a valid solution")  #checks whether a column is valid
            break
    for i in list(range(0,3)): 
        for j in list(range(0,3)):
           if not validrow(blocksTorows([l[i],l[i+1],l[i+2]])[j]):
               print("Not a valid solution")  #checks whether a block is valid
               break
        
        
            
           