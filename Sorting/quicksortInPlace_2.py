#quicksort inplace 2 sided
def quicksort2(l,b,e):
    if e-b < 1:
        return l
    p=l[b]
    left=b+1
    right=e
    while(right>=left):
        if l[left]<p:
            left=left+1
        elif l[right]>=p:
            right=right-1
        else:
            l[left],l[right]=l[right],l[left]
            left=left+1
            right=right-1
    if left > b+1 :
       l[b],l[left-1] = l[left-1],l[b]
       quicksort(l,b,left-2)
       quicksort(l,left,e)
    else:
       quicksort(l,b+1,e)
    return l  