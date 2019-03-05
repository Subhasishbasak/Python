import re
import urllib.request

#p = re.compile(r'<[a-z]+\s.*href="(http.*)">')
p = re.compile(b'<[a-z]+\s[^>]*href="(http[^>]*)">')
with urllib.request.urlopen("http://www.fsttcs.org/papers.php") as f:
  ls = f.read()
  m = p.finditer(ls)
  for x in m:
    print(x.group(1))

