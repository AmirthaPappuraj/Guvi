import decimal
def roundoff(n):
  digit=5
  temp=str(decimal.Decimal(str(n)+'0' * digit))
  return temp[:temp.find('.')+digit+1]

n1,n2=map(float,input().split())
a=n1*n2
result=roundoff(a)
print(result)
