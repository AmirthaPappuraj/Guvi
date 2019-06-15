num=int(input())
sr,er=map(int,input().split())
for i in range (sr,er):
  if num==i:
    print('yes')
    break
else:
  print('no')
