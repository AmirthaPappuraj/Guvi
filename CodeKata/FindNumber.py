text=input()
a=any(char.isdigit() for char in text)
if(a==1):
  print('Yes')
else:
  print('No')
