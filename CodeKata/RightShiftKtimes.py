a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(0,a[1]):
  b=[b[-1]] + b[:-1]
print(*b,end=' ')
