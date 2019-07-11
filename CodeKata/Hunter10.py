n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=1
for i in b:
  if i not in a:
    print("NO")
    c=0
    break
if(c==1):
  print("YES")
