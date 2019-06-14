import re
t=input()
count=len(t)-len(re.findall('[\w]',t))
print(count)
