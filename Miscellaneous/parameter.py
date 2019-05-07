x = 5

def f(y):
   y = y+1
   return y

print(f(x))
print(x)

print(".........")

l = [3,4,5]

def g(ls):
    ls = [3,2]
    return ls

print(l)
print(g(l))
print(l)  

print(".........")

def h(ls):
    ls[0] = 10
    return ls

print(l)
print(h(l))
print(l)

l = [3,4,5]
print(l)
print(h(l[:])

