import re
line=input()
spch=len(line)-len(re.findall('[\w]',line))
print(spch)
