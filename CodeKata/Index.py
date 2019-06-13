count=int(input())
l=list(map(int,input().split()))
if(len(l)==count):
  for i in range(count):
    print(l[i],i)
