from priorityQclassv2 import *

def process(ls):
  q1 = priorityQ()
  q2 = priorityQ()
  for x in ls:
    (p,i) = x
    if i >= 0 and p == 1:
      q1.insert(i) 
    elif i >= 0 and p == 2:
      q2.insert(i)
    elif i < 0 and p == 1:
      if q1.isempty():
        print("No bids available")
      else:
        print(q1.deletemin())
    elif i < 0 and p == 2:
      print(q2.deletemin())

      
