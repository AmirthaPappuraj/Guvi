import math
n=float(input())
res=math.radians(n)
if(res>0 and res<1):
  print(round(math.sin(res),2))
else:
  print(round(math.sin(res)))
