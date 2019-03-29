from priorityQ import *

def process(ls):
  for i in ls:
    if i >= 0: 
      insert(i)
    elif isempty():
      print("No bids available")
    else:
      print(deletemin())

      
