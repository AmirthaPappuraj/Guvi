num=input()
for i in num:
  if(i=='/'):
    c=num.split('/')
    print(int(int(c[0])/int(c[1])))
  elif i=='%':
    c=num.split('%')
    print(int(int(c[0])%int(c[1])))
