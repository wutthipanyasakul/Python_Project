# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 04:38:31 2024

@author: satha
"""

#challenges: control flow 6

#In Range

"""
Define the function to accept three numbers as parameters
Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound
If this is true, return True, otherwise, return False
"""

def in_range(num, lower, upper):
    if (num >= lower) and (num <= upper):
        return True
    else:
        return False

print(in_range(10, 10, 10))
# should print True

print(in_range(5, 10, 20))
# should print False
        