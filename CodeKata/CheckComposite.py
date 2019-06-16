n=int(input())
f=0
for i in range(1,n):
  if(n%i)==0:
    f=i
if f>1:
  print('yes')
elif n==1:
  print('no')
else:
  print('no')
