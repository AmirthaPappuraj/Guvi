def palin(s):
  rev=s[::-1]
  if(s==rev):
    print('yes')
  else:
    print('no')
s=input()
palin(s)
