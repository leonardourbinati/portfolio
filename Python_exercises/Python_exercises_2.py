# 2.1
x= 'fire and ice'
print('x= %s' %x)

# 2.2
print('\nthird character of x= %s' %x[2])

# 2.3
print('\nfifht character of x= %s' %x[4])

# 2.4
print('\ntenth character of x= %s' %x[9])
print('last character of x= %s' %x[-1])
print('second to last character of x= %s' %x[1:])

# 2.5
print('\n')
for E in range(len(x)):
	if E%2==0:
		print('character in odd position= %s' %x[E])
# 2.6
	else:
		print('character in even position= %s' %x[E])

# 2.7
print('\nfirst half of the string= %s' %(x[0:(len(x)/2)]))

# 2.8
print('\nstring in reverse= %s' %x[::-1])

# 2.9
i= x.count('i')
e= x.count('e')
print("\n'i' words in x= %s" %i)
print("'e' words in x= %s" %e)

# 2.10
x= x.replace('and','&')
if '&' in x:
	print("\n'and' replaced with '&'")
	print('current x= %s' %x)
else:
	print("\n'and' not replaced with '&'")

# 2.11
if 'fire' in x:
	print("\ncheck for word 'fire'= ok")
else:
	print("\ncheck for word 'fire'= not ok")

# 2.12
if 're and' in x:
	print("\ncheck for word 're and'= ok")
else:
	print("\ncheck for word 're and'= not ok")

# 2.13
if 're &' in x:
	print("\ncheck for word 're &'= ok")
else:
	print("\ncheck for word 're &'= not ok")

# 2.14
print("\nposition of the first 'e'= %s" %(x.find('e')))

# 2.15
print("\nposition of the last 'e'= %s" %(x.rfind('e')))

# 2.16
x= 'sun and clouds'
print('\ncurrent x= %s' %x)
print('third character of x= %s' %x[2])
print('fifht character of x= %s' %x[4])
print('tenth character of x= %s' %x[9])
print('last character of x= %s' %x[-1])
print('second to last character of x= %s' %x[1:])
for E in range(len(x)):
	if E%2==0:
		print('character in odd position= %s' %x[E])
	else:
		print('character in even position= %s' %x[E])

print('first half of the string= %s' %(x[0:(len(x)/2)]))
print('string in reverse= %s' %x[::-1])
i= x.count('i')
e= x.count('e')
print("'i' words in x= %s" %i)
print("'e' words in x= %s" %e)
if x.rfind('e')==-1:
	print("no 'e' characters found in x")
else:
	print("position of the last 'e'= %s" %(x.rfind('e')))

# 2.17
x1= "234432976548923"
print('\ncurrent x= %s' %x1)

# 2.18
y1= " "
for E in x1:
	int(E)+3
	z1= int(E)+3
	y1= y1+str(z1)
print('\nvalues of x increased by 3= %s' %y1)
