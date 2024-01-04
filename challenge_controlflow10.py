# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 05:06:29 2024

@author: satha
"""

#Challenges: control flow 10

#Max Number
"""
Define a function that has three input parameters, num1, num2, and num3
Test if num1 is greater than the other two numbers
If so, return num1
Test if num2 is greater than the other two numbers
If so, return num2
Test if num3 is greater than the other two numbers
If so, return num3
If there was a tie between the two largest numbers, then return "It's a tie!"

"""

def max_num(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        return num1
    elif (num2 > num1) and (num2 > num3):
        return num2
    elif (num3 > num1) and (num3 > num2):
        return num3
    else:
        return "It's a tie!"

print(max_num(-10, 0, 10))
# should print 10

print(max_num(-10, 5, -30))
# should print 5

print(max_num(-5, -10, -10))
# should print -5

print(max_num(2, 3, 3))
# should print "It's a tie!"



