n=int(input())
a=list(map(str,input().split()))
b=[]
for i in range(len(a)):
  if(a[i]==str(i)):
    b.append(a[i])
if(len(b)==0):
  print("-1")
else:
  print(' '.join(sorted(b)))
