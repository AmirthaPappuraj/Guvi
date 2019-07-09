n=int(input())
a=list(map(str,input().split()))
x=sorted(a,reverse=True)
print(''.join(x))
