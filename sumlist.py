y = [1,9,5,0,20,-4,12,16,7]
len(y)
suma = 12
for i in range(0,len(y)):

  for j in range(i+1,len(y)):
      res=y[i]+y[j]

      if res == suma:
        print(y[i], ", ", y[j])

