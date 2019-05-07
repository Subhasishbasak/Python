marklist = [("Abcd", 32), ("Afgh",42), ("ijkl",44), ("mnop",29),("qrst",40)]

def passed(ml):
  ans = []
  for i in ml:
    name,marks = i
    if marks >= 35:
      ans.append(i)
  return(ans)

print(passed(marklist))

def passfn(v):
  name,marks = v
  if marks >= 35:
    return True
  else:
    return False

passedList = list(filter(passfn,marklist))

def incbyFive(v):
   name,marks = v
   return(name,marks+5)

print(list(map(incbyFive,passedList)))
print(passedList)



