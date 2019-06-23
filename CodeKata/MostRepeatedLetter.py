ASCII_SIZE = 256
def frequent(a): 
	count = [0] * ASCII_SIZE  
	max = -1
	c = '' 
	for i in a: 
		count[ord(i)]+=1; 
	for i in a: 
		if max < count[ord(i)]: 
			max = count[ord(i)] 
			c = i 
	return c  
s = input()
print (frequent(s))
