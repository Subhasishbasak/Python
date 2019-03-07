from priorityQheap import *

try:
  h = priorityQ()
  h.insert(3)
  h.insert(4)
  print(h.deletemin())
  print(h.deletemin())
#  print(h.deletemin())
  print("I am here")
except priorityQ.HeapEmptyException:
  print("Oops I tried to delete from an Empty Heap")
finally:
  print("I will print this always")
