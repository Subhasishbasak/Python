L = ["This", "That", "this", "This", "that"]

wc = {}
for i in L:
  try:
    wc[i] = wc[i] + 1
  except KeyError:
  #:except Exception:
    wc[i] = 1
print(wc.items())
