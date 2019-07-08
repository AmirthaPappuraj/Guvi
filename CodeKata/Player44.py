a,b= list(map(str,input().split()))
b=int(b)
for i in range(b):
  c= ""
  c += a[-1]
  for i in range(len(a)-1):
    c+= a[i]
  a= c
print(a)
