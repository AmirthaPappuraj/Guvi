num1,num2=map(int,input().split())
if(num1>num2):
  c=num1
else:
  c=num2
while(1):
  if(c%num1==0 and c%num2==0):
    print(c)
    break
  c=c+1
