# 1.1
x= 7
print('x= %s' %x)

# 1.2
y= 3.14
print('\ny= %s' %y)

# 1.3
z= x%2
if z==0:
	print("\n%s is even" %x)

else:
	print("\n%s is odd" %x)

# 1.4
mean1= (x+y)/2
print('\nmean(x, y)= %s' %mean1)

# 1.5
d1= x-mean1
d2= y-mean1
print('\nd(x)= %s' %d1)
print('d(y)= %s' %d2)

# 1.6
mean2= (d1+d2)/2
print('\nmean(d(x), d(y))= %s' %mean2)

# 1.7
x= x*2
print ('\ncurrent x= %s' %x)
w= x-1
print('w= x-1= %s' %w)

# 1.8
print('\nx= %s' %x)


y= 3.14
print('y= %s' %y)


z= x%2
if z==0:
	print("%s is even" %(x))

else:
	print("%s is odd" %(x))


mean1= (x+y)/2
print('mean(x, y)= %s' %mean1)


d1= x-mean1
d2= y-mean1
print('d(x)= %s' %d1)
print('d(y)= %s' %d2)

# 1.9
from random import randint
x1= randint(1,100)
x2= randint(1,100)
y1= randint(1,100)
y2= randint(1,100)
print('\nx1= %s' %x1)
print('x2= %s' %x2)
print('y1= %s' %y1)
print('y2= %s' %y2)
print('A(%s,%s)' %(x1, y1))
print('B(%s,%s)' %(x2, y2))

# 1.10
from math import sqrt
D= sqrt((x1-x2)**2+(x2-y2)**2)
print ('\nEuclidean distance (A, B)= %s' %D)

# 1.11
from random import random
p= random()
print('\np= %s' %p)
from math import log2
IC= -log2(p)
print('I.C.= %s' %IC)

# 1.12
for every in range(3):
	x1= randint(1,100)
	x2= randint(1,100)
	y1= randint(1,100)
	y2= randint(1,100)
	print('\nx1= %s' %x1)
	print('x2= %s' %x2)
	print('y1= %s' %y1)
	print('y2= %s' %y2)
	print('A(%s,%s)' %(x1, y1))
	print('B(%s,%s)' %(x2, y2))
	D= sqrt((x1-x2)**2+(x2-y2)**2)
	print ('Euclidian distance (A, B)= %s' %D)
	p= random()
	IC= -log2(p)
	print('p= %s' %p)
	print('I.C.= %s' %IC)
