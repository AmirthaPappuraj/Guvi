a=int(input())
b=0
c=[]
for i in range(a):
  c.append(input())
for i in range(a):
  if(sorted(c[i])==sorted('kabali')):
    b=b+1
print(b)
