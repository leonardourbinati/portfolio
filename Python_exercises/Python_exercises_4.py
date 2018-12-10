# 4.1
x= [4,8,-9,'the']
y= ['silent force',4.67,9]
z= x+y
print z

# 4.2
if 'the' in x:
	print("\ncheck for word 'the'= ok")
else:
	print("\ncheck for word 'the'= not ok")

if 'silent force' in y:
	print("\ncheck for word 'silent force'= ok")
else:
	print("\ncheck for word 'silent force'= not ok")

# 4.3
k= '23|64|354|-123'
print('\n')
print(k.split('|'))

# 4.4
print('\nstring= -1-987-6823-8261')
j= '-1-987-6823-8261'
if j[0]!='-':
	print('\npositive numbers= %s' %(j[0]))
for i in range(len(j)):
	if j[i]!='-' and j[i+1]!='-':
		print('positive numbers= %s' %(j[i+1]))

# 4.5
h= [3.14,6.333,98.12,23.1]
print('\nlist= [3.14,6.333,98.12,23.1]')
print('list to string: %s' %(','.join(str(e) for e in h)))

# 4.6
LIST= input('\ndigit a list of elements: ')
def addlist(LIST):
	STRING_JOIN= ''.join(str(e) for e in LIST)
	return STRING_JOIN
print("list elements' sum= %s" %(addlist(LIST)))
