# Emanuel Ramos
# 11/08/2022
#
# Problem 4: this program calculates the area of a circle when given the radius using pi from the math module

import math

# The program requires the input of the "radius" of the circle, so it can run.
r = int(input("what is the radius of the circle?\n"))
input("press 'enter' to continue\n")

# This is the equation on how to get the area of a circle given the "Area".
A = math.pi * r ** 2

# The radius inputted will be displayed as well as the area that the program calculated.
print("This is the radius:", r)
print("This is the area of the circle:", A)
