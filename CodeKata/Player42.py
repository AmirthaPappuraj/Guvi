n=int(input())
a=list(map(int,input().split()))
c=a
a.sort()
if a==c:
    print("yes")
else:
    print("no")
