count=int(input())
l=map(int,list(input().split()))
s=sorted(l)
for i in range (0,len(s)):
  print(s[i],end=' ')
