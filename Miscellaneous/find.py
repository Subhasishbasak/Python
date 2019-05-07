x = [3,4,1,2,2,1,3,5,6,2]
v = 2

a = 0
pos = -1
for i in x:
  if i == v and pos == -1:
    pos = a
  a = a + 1
print(pos)

pos = -1
for i in list(range(0,len(x))):
   if x[i] == v  and pos == -1:
      pos = i
print(pos)  

pos = -1
i = 0
while (i < len(x)):
  if x[i] == v and pos == -1:
     pos = i
  i = i+1
print(pos)

pos = -1
i = 0
while (i < len(x) and pos == -1)
  if x[i] == v and pos == -1:
     pos = i
  i = i+1
print(pos)
