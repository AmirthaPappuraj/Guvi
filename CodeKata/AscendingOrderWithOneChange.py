n=int(input())
l=list(map(int,input().split()))
a=l[0]
if n==len(l):
  for i in range(1,len(l)):
    if l[i]>a:
      a=l[i]
    else:
      print(i-1)
      break
