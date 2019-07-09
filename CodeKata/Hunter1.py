n=int(input())
l=list(map(int,input().split()[:n]))
s=[]
for i in range(0,n+1):
   if(l.count(i)>1):
      s.append(i)
if(len(s)==0):
   print("unique")
res=sorted(s)
print(' '.join(map(str,res)))
