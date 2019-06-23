a=int(input())
b=input()
temp=0
v=['a','e','i','o','u']
for i in v:
  if(i in v):
    b=b.replace(i,'')
print(b[::-1])
