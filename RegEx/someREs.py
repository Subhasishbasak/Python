import re
p1 = re.compile(r" l.*g ") # First attempt at words beg with l and ending with g 
p2 = re.compile(r" l[^ ]*g ") # Second attempt. cannot skip over whitespace 
p3 = re.compile(r" l\S*g ")   # \S = not whitespace \s = whitespace
print(p3.match(" long loong looong"))
p3.findall( "long loong looong")
x = p3.match(" long loong looong")
print(x.group())

p4 = re.compile(r"\S+") # \S = non-white space. So, splits into words
print(p4.findall("This is a sentence with 7 words"))

# Union. ending with g or s
p5 = re.compile(r"\S*g|\S*s")
print(p5.findall("This iss a longgg sentence digger"))
p6 = re.compile(r"\S*g\s|\S*s\s") # ensuring we pick full words
print(p6.findall("This iss a longgg sentence digger"))

#Forming groups within the pattern
p7 = re.compile(r"a*(b*)(d*)e")
x= p7.match("abde")
print(x.group(0)) # Full matched pattern
print(x.group(1)) # The subpattern matching (b*), the first group
print(x.group(2)) # The subpattern matching (d*), the second group
x= p7.match("aaaabbbdddddde")
print(x.group(0)) # Full matched pattern
print(x.group(1)) # The subpattern matching (b*), the first group
print(x.group(2)) # The subpattern matching (d*), the second group

p8 = re.compile(r"(a*)(b*)(d*)e")
x= p8.match("aaaabbbdddddde")
# Now there are 3 groups.

p9 = re.compile(r"\s+\d+\s+")
print(p9.findall("This 235 is an integer b2838 is not and 28 is"))
