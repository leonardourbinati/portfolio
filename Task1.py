# This script calculates the volume of a sphere and prints it to the screen
from math import pi
diameter= input("type the diameter of the sphere for which you want to calculate the volume: ")
radius= float(diameter)/2
volume= (4.0/3)*(pi)*(radius**3)
print ("Volume of a sphere: %s" %(volume))
