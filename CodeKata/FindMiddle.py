def findmiddle(n):
  m=float(len(n))/2
  if m%2 != 0:
    return n[int(m-0.5)]
  else:
    return (n[int(m)],n[int(m-1)])

num=input()
num1=list(num)
mid=findmiddle(num1)
print(mid)
