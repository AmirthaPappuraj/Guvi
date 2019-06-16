def iso(a):
  c=a.lower()
  l=[]
  for i in c:
    if i in l:
      return 'no'
    l.append(i)
  return 'yes'

char=input()
res=iso(char)
print(res)
