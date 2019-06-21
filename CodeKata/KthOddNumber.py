num1,num2=map(int,input().split())
li=list(map(int,input().split()))
if li[num2]%2!=0:
    print(li[num2])
else:
    print(li[num2-1])
