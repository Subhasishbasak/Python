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
    