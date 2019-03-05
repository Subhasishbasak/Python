import re

p = re.compile(r'(<[a-z]+\s[^>]*href=")(http[^>]*)(">)')
with open("FSTTCSAP.html","r") as f:
  ls = f.read()
  print(p.sub(r'\1http://wwww.google.com\3',ls))

