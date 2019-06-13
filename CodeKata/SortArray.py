n=int(input())
l1=map(int,list(input().split()))
new=sorted(l1)
for x in range(0,len(new)):
  print(new[x], end=' ')
