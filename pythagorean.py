# Emanuel Ramos
# 11/08/2022
#
# Problem 5: this program does the pythagorean theorem equation using the math module

import math

# ask the user for "a" and "b" from the pythagorean theorem
a = int(input('what is "a"?'))
b = int(input('what is "b"'))
input("press 'enter' to continue\n")

# do the pythagorean theorem equation using the math module functions
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

# print values inputted for "a" and "b"
print('This is "a":', a)
print('This is "b":', b)

# print the answer to the pythagorean theorem equation using the inputs
print('This is the answer to the equation:', c)
