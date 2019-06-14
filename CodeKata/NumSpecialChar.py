import re
line=input()
sc=len(line)-len(re.findall('[\w]',line))
print(sc)
