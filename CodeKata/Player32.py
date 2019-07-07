n1,n2=map(int,input().split())
list1=list(map(int,input().split()))
c=0
for i in list1:
    if i==n2:
        c=1
if c==1:    
     print("Yes")
else:
    print("No")
