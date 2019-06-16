def iso(a):
  c=a.lower()
  l=[]
  for i in c:
    if i in l:
      return 'No'
    l.append(i)
  return 'Yes'

char=input()
res=iso(char)
print(res)
