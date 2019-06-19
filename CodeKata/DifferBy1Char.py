def check(string1,string2):
  if len(string1) == len(string2):
    count_diffs = 0
    for a, b in zip(string1, string2):
        if a!=b:
            if count_diffs: 
              return ('no')
            count_diffs += 1
    return ('yes')
  else:
    exit()

a,b=map(str,input().split())
res=check(a,b)
print(res)
