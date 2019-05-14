#Practice problem 2
#Q.1

def inpins(l):
    def cmp(a,b):
    x,y=a
    p,q=b
    if x>p:             #put >= for unstable version
        return True
    else:
        return False
    for i in range(0,len(l)):
        key=l[i]
        j=i-1
        while(j>=0 and cmp(l[j],key)):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
    return l    

inpins([(9,"a"),(8,"b"),(6,"c"),(2,"d"),(3,"e"),(6,"f"),(1,"f")])

#Q.2
#Quicksort inplace iterative

def quicksort_it(l):
     if len(l)<2:
         return l
     x=set(l)
     for i in x:
         left=0
         right=len(l)-1
         while(right>=left):
             if l[left]<i:
                left=left+1
             elif l[right]>=i:
                right=right-1
             else:
                l[left],l[right]=l[right],l[left]
                left=left+1
                right=right-1
         print(l)
     return l 
    


#Q.3
     
def quicksort_it2(l):
     def cmp(a,b):
        x,y=a
        p,q=b
        if x>=p:             #stable always
            return True
        else:
            return False
     if len(l)<2:
         return l
     x=set(l)
     for i in x:
         left=0
         right=len(l)-1
         while(right>=left):
             if not cmp(l[left],i):
                left=left+1
             elif cmp(l[right],i):
                right=right-1
             else:
                l[left],l[right]=l[right],l[left]
                left=left+1
                right=right-1
         print(l)
     return l   

quicksort_it2([(9,"a"),(8,"b"),(6,"c"),(2,"d"),(3,"e"),(6,"f"),(1,"f")])
 
#Q.4
#import string
def bucket(l,i):
    ans=[]
    l1=[]
    for j in l:
        if len(j)<i+1:
            ans.append(j)
        else:
            l1.append(j)
    for j in string.ascii_uppercase+string.ascii_lowercase:        
       for k in l1:
           if k[i]==j:
               ans.append(k)
    return ans
  
#bucket has complexity O(53n)=O(n)  

def bucketsort(l):
    ans=[]
    for i in string.ascii_uppercase+string.ascii_lowercase:  
        temp=[]
        for j in bucket(l,0):
            if j[0]==i:
                temp.append(j)
        k=1
        while(temp!=bucket(temp,k)):       
            temp=bucket(temp,k) 
            k=k+1
        if temp!=[]:    
            ans.append(temp) 
    return(sum(ans,[])) 
    
#bucket has complexity O(n^2)  
    
    
#Q.5

def sumfree(n):
      def check(l,v):
          l=set(l)
          for i in l:
              if (v-i) in l-{i}:
                  return False
          return True 
      temp=[]
      ans=[[]]
      for k in list(range(1,n+1)):
          for j in ans:
             if check(j,k):
                  temp.append(j+[k])
          ans=ans+temp 
          temp=[]
      return ans

#Q.6
            
def nextpermutation(l):
    i=-1
    while(i>-len(l)):
        if l[i]>l[i-1]:
            l[-1],l[i-1]=l[i-1],l[-1]
            l1=l[len(l)+i:]
            l1.reverse()
            return (l[:len(l)+i] + l1) 
        i=i-1   
    return []    


     
