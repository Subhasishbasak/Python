import re

p = re.compile(b'<[a-z]+\s.*href="(http.*)">')
#p = re.compile(b'<[a-z]+\s[^>]*href="(http[^>]*)">')
with open("FSTTCSAP.html","br") as f:
  ls = f.read()
  m = p.finditer(ls)
  for x in m:
    print(x.group(1))

