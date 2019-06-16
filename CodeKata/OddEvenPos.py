text=input()
l=list(text)
odd=list()
even=list()
i=0
for x in l:
  if i%2 == 0:
    odd.append(x)
  else:
    even.append(x)
  i+=1
stringodd="".join(odd)
stringeven="".join(even)
print(stringodd,stringeven, end=' ')
