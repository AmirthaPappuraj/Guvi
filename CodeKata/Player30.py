a,b,c =list(map(str,input().split()))
c=int(c)
count=0
for i in range (len(a)):
  if a[i]!=b[i]:
     count=count+1
if(count==c):
     print("yes")
else:
  print("no")
