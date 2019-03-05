import re

ls = '''
This is a long sentence, of more than 20 letters and 8 words. I may have real numbers such as 3.14 in this, but it should not print them out. But integers can be the last word in a sentence such as 30. The word a39b contains the integer 39..45 and .382. Does it work with .45?
'''

p = re.compile(r'\S\S\S\S\S\S\S*') # any word with at least 6 letters
print(p.sub("LongWordWasHere",ls))
