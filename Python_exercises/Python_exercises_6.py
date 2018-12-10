'''# 6.1
x=list(range(3,13))
print ('x= %s' %x)

# 6.2
print('\n')
for e in x:
	if e%2==0:
		print('even numbers= %s' %e)
	else:
		print('odd numbers= %s' %e)

# 6.3
print('\n')
for e in x:
	if e%5==0:
		print('multiples of 5= %s' %e)

# 6.4
x=list(range(8,24))
print ('\nx= %s' %x)

# 6.5
print('\n')
for e in x:
	y= (((e*2)-2)/3.0)
	print ('((x[e]*2)-2)/3= %s' %y)

print ('\nx values sum= %s' %(sum(x)))

# 6.6
k= [5,2,7,8,1,-3]
print('\nk= %s' %k)

# 6.7
print('\nfirst and third value of k= %s, %s' %(k[0], k[2]))

# 6.8
print('\n')
for e in k:
	h= e*2
	print('k[e]*2= %s' %h)

# 6.9
print('\n')
for e in k:
	p= (((e*2)-2)/3.0)
	print ('((k[e]*2)-2)/3= %s' %p)

# 6.10
print ('\nk values sum= %s' %(sum(k)))

# 6.11
print('\nminimun value of k= %s' %(min(k)))

# 6.12
print('\nmaximum value of k= %s' %(max(k)))

# 6.13
n= sum(k)/float(len(k))
print('\naverage of k= %s' %n)'''

# 6.14
a='avocado'
r='radar'
print('\na= %s' %a)
print('r= %s' %r)

# 6.15
a1=list(a)
r1=list(r)
a2= a1[::-1]
r2= r1[::-1]
for e in a2:
	a3=''.join(str(e) for e in a2)
print("\n'avocado' reverse= %s" %a3)
for e in r2:
	r3=''.join(str(e) for e in r2)
print("'radar' reverse= %s" %r3)

# 6.16
if (list(a)[:])==(list(a)[::-1]):
	print('\na= palindrome string')
if (list(r)[:])==(list(r)[::-1]):
	print('\nr= palindrome string')

# 6.17
print('\nfirst half of a= %s' %(list(a)[0:len(a)/2]))
print('second half of r= %s' %(list(r)[len(r)/2:]))

# 6.18
print('\n')
string1= raw_input('digit first DNA string: ')
string2= raw_input('digit second DNA string: ')
string1= string1.upper()
string2= string2.upper()
print('\nfirst DNA string= %s' %string1)
print('second DNA string= %s' %string2)
