n1,n2=map(int,input().split())
flag=0
for i in  range(1,n1):
    if n2**i==n1:
        flag=1
        break
if flag==1:
    print("yes")
else:
    print("no")
