n=int(input())
fv=0
sv=1
for i in range(1,n+1):
  if(i<=1):
    tv=i
  else:
    tv=fv+sv
    fv=sv
    sv=tv
  print(tv,end=' ')
