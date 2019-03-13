x = 5

def f():
   x = 7
   def g():
     global x
     x = 8
     print(x)
   g()
   print(x)

f()
print(x)

   
