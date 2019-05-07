x = [3,4,1,2,2,1,3,5,6,2]
v = 2

pos = -1
i = 0
while (i < len(x)):
  if x[i] == v:
    pos = i
    break
  i = i+1
print(pos)



