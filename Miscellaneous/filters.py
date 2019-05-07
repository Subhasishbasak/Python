
def f(n):
   if (n > 50):
     return True
   else:
     return False

l = [2,100,29,97,33,38,59,67]

print(list(filter(f,l)))
