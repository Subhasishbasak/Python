def process(ls):
  l1 = []
  l2 = []
  for x in ls:
    (p,i) = x
    if i >= 0 and p == 1:
      l1.append(i)  # Add bid to current list of available bids
    elif i >= 0 and p == 2:
      l2.append(i)
    elif i < 0 and p == 1:
      mpos = 0
      mval = l1[0] 
      for j in range(1,len(l1)):
        if l1[j] < mval:
          mval = l1[j]
          mpos = j
      print((p,mval))
      # Delete this occurrence of the  minimum value
      l1 = l1[:mpos]+l1[mpos+1:] 
    elif i < 0 and p == 2:
      mpos = 0
      mval = l2[0] 
      for j in range(1,len(l2)):
        if l2[j] < mval:
          mval = l2[j]
          mpos = j
      print((p,mval))
      # Delete this occurrence of the  minimum value
      l2 = l2[:mpos]+l2[mpos+1:] 

      
