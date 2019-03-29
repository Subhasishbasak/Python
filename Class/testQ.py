from priorityQclassv2 import *

x = priorityQ()
x.insert(3)
x.insert(5)
print(x.deletemin())
x.isempty()
print(x.__findmin())
