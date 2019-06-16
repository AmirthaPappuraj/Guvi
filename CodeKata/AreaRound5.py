import decimal

def roundoff(x):
  d=5
  temp=str(decimal.Decimal(str(x)+'0' * d))
  return temp[:temp.find('.')+d+1]

num1,num2=map(float,input().split())
area=num1*num2
output=roundoff(area)
print(output)
