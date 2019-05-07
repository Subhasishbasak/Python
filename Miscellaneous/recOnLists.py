def mylen(l):
  if l == []:
    return 0
  else:
    return 1 + mylen(l[1:])
