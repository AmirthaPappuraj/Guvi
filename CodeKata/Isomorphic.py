maxch=256
def iso(a,b):
  m=len(a)
  n=len(b)
  if m!=n:
    return ('no')
  ma=['no']*maxch
  map=[-1]*maxch
  for i in range(n):
    if map[ord(a[i])]==-1:
      if ma[ord(b[i])]=='yes':
        return('no')
      ma[ord(b[i])]='yes'
      map[ord(a[i])]=b[i]
    elif map[ord(a[i])]!=b[i]:
      return('no')
  return('yes')

a,b=map(str,input().split())
res=iso(a,b)
print(res)
