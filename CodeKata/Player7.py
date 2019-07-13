a=list(input())
l=len(a)
b=[]
for i in range(0,l,2):
  b.append(a[i+1])
  b.append(a[i])
print(*b,sep='')
