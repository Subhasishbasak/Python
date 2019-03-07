while True:
  try:
    x = int(input("Please enter an Integer\n"))
    print("You Typed: ")
    print(x)
    break
  except ValueError:
    print("That is Not an integer")

