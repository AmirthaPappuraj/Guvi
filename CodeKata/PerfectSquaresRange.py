def Squares(a, b): 
  c = 0 
  for i in range (a, b + 1): 
    j = 1; 
    while j * j <= i: 
      if j * j == i: 
        c =c + 1
      j = j + 1
    i = i + 1
  return c 
a,b=map(int,input().split())
c=Squares(a,b)
print(c)
