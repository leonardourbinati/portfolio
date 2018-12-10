# 3.1
x= float(input('input x= '))
def increase(n):
	n= x+1
	return n
print('x+1= %s' %increase(x))

# 3.2
x1= float(input('input x1= '))
x2= float(input('input x2= '))
def add(x1,x2):
	n= x1+x2
	return n
print('x1+x2= %s' %add(x1,x2)) 

# 3.3
x3= float(input('input x3= '))
def add3(x1,x2,x3):
	n= x1+x2+x3
	return n
print('x1+x2+x3= %s' %add3(x1,x2,x3))

# 3.4
x4= float(input('input x4= '))
x5= float(input('input x5= '))
def add5(x1,x2,x3,x4,x5):
	n= x1+x2+x3+x4+x5
	return n
print('x1+x2+x3+x4+x5= %s' %add5(x1,x2,x3,x4,x5))

# 3.5
number= input('input a number= ')
string= raw_input('input a word= ')
def string_per_number(number,string):
	z= string*number
	return z
print('word_for_n_times= %s' %string_per_number(number,string))

# 3.6
def string_per_number(number,string):
	comma=","
	new_string= string+comma
	z= (new_string*(number-1))+string
	return z
print('word_for_n_times= %s' %string_per_number(number,string))

# 3.7
separator= raw_input('input a separator= ')
def string_per_number(number,string):
	new_string= string+separator
	z= (new_string*(number-1))+string
	return z
print('word_for_n_times= %s' %string_per_number(number,string))
