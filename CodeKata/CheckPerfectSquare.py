import math
num1,num2=map(int,input().split())
mul=num1*num2
r=math.sqrt(mul)
if int(0.5+r)**2 ==mul:
  print('yes')
else:
  print('no')
