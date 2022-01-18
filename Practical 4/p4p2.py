import math
length = float(input("Enter length of side:"))
print('\n')
print("The length chosen is", length, '\n')

#area of square with this side length 
print("the area of the square with side of this length:", length**2, '\n')

#volume of a cube with this side length
print("the volume of the cube with side of this length:", length**3, '\n')

#area of a circle with radius of this length
print("the area of the circle with radius of this length:", math.pi*length**2, '\n')

#volume of a sphere with radius of this length 
print("the volume of the sphere with radius of this length:", (4/3)*math.pi*length**3, '\n')

#volume of a cylinder with radius of this length and side of this length
print("the volume a cylinder with radius of this length and side of this length:",
      math.pi*length**2*length, '\n')
