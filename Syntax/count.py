L = ["This", "That", "this", "This", "that"]

wc = {}
for i in L:
  if i in wc.keys():
    wc[i] = wc[i] + 1
  else:
    wc[i] = 1
print(wc.items())
