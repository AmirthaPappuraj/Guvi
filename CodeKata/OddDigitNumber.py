num=input()
l=list(num)
for i in range(0,len(l)):
  if (int(l[i])%2)!=0:
    print(l[i], end=' ')
