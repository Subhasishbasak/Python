def splitwith(s,c):
  ans = []
  curr = ""
  for i in s:
    if i == c:
      ans.append(curr)
      curr = ""
    else:
      curr = curr + i
  ans.append(curr)
  return(ans)

