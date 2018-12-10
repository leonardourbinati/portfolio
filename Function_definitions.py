#This function gives the distance of two point (P1, P2)

from math import sqrt, pow

P1= [x1,y1]= [float(input('input x1: ')), float(input('input y1: '))]
P2= [x2,y2]= [float(input('input x2: ')), float(input('input y2: '))]

def distance(P1,P2):
	distance= sqrt(pow((x1-x2),2)+pow((y1-y2),2))
	return distance

print('distance(P1,P2)= %s' %(distance(P1,P2)))

#This function gives the value of a scalar by point given a scalar "a" and a point p= (px, py)

a= float(input('\ninput the scalar number: '))
p= [px,py]= [float(input('input px: ')), float(input('input py: '))]

def scalar_by_a_point(a,p):
	scalar= a*px, a*py
	return scalar

print('scalar by a point= (%s, %s)' %(scalar_by_a_point(a,p)))

#This function gives the solutions of a binomial equation given parameters a, b, c

a = float(input("\ntype the first parameter of a 2nd degree equation: "))
b = float(input("type the second parameter of a 2nd degree equation: "))
c = float(input("type the third parameter of a 2nd degree equation: "))

from math import sqrt

def roots_of_equation(a, b, c):
	'''Input: the three parameters a, b, c; Output: the roots
	of a 2nd degree equation'''
	
	root1 = - b - sqrt(b**2 - 4*a*c)/2*a
	root2 = - b + sqrt(b**2 - 4*a*c)/2*a
	return float(root1), float(root2)

print('x1, x2= %s, %s' %(roots_of_equation(a, b, c)))
