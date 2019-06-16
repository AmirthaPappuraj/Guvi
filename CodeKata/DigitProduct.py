n=int(input())
p=1
while(n!=0):
  p=p*(n%10)
  n=n//10
print(p)
