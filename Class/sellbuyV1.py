def process(ls):
  l = []
  for i in ls:
    if i >= 0: 
      l.append(i)  # Add bid to current list of available bids
    else:
      # find the minimum in l, report and delete
     
      # Find the minimum and its location
      mpos = 0
      mval = l[0] 
      for j in range(1,len(l)):
        if l[j] < mval:
          mval = l[j]
          mpos = j

      # report the minimum value
      print(mval)

      # Delete this occurrence of the  minimum value
      l = l[:mpos]+l[mpos+1:] 

      
