try:
  x = int(input())
  print(x)
except KeyError:
  print("oops that is not an integer")
except ValueError:
  print("Not an Integer")
