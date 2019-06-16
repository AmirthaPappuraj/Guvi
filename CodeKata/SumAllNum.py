num=int(input())
l=list(map(int,input().split()))
res=0
for x in range(0,num):
  res=res+l[x]
print(res)
