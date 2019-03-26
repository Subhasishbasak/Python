def insert(v,l):  # assume input is of length i
  cpos = 0       # 1 step
  while cpos < len(l) and l[cpos] < v :  # worst case, i steps
     cpos = cpos + 1
  return l[:cpos] + [v] + l[cpos:]  # i+1 steps

# insert on input i takes 1 + i + i+1 = 2i + 2 steps


def insertionsort(l):   # l is of length N
  ans = []              # 1 step
  while l :  # 1 + insert(0) + 1 + insert(1) + 1 + insert(2) ... 1 + insert(N-1)
    v = l.pop()           # 1 step
    ans = insert(v, ans)  # in the ith iteration length of ans is i-1
  return(ans)

# 1 + (2.0 + 2) + 1 + (2.1 + 2) + ...  1 + 2(N-1) + 2
# 3.(N-1) + 2(0 + 1 + 2 .. N-1)
# 3.(N-1) + 2(N(N-1)/2) 
# O(N^2)
