#Insersion sort inplace
def inpins(l):
    for i in range(0,len(l)):
        key=l[i]
        j=i-1
        while(j>=0 and l[j]>=key):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
    return l    

inpins([9,8,6,2,3,2,1])
