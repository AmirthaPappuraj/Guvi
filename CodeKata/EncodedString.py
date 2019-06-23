a=input()
b='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
c=''
for i in a:
  if i in b:
    t=b.index(i)
    t=t+3
    c=c+b[t]
print(c)
