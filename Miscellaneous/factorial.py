def fact(n):
  ans = 1
  for i in range(1,n+1):
    ans = ans * i
  return ans

def factw(n):
  ans = 1
  while (n > 0):
    ans = ans * n
    n = n-1
  return(ans)

x = 5
print(factw(x))
print(x)

def factr(n):
  if n == 0:
    return 1
  else:
    ans = n * factr(n-1)
    return ans

