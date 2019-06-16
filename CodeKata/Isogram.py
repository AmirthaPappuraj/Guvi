def iso(a):
  if(type(a)==str):
    for i in a:
      if a.count(i)>1 or a=='':
        return('no')
      else:
        return('yes')

char=input()
res=iso(char)
print(res)
