# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 04:29:00 2024

@author: satha
"""

#challenges: control flow 3

#Large Power

"""
create a function that tests
 whether the result of taking the power of one number to another number provides an answer 
 that is greater than 5000
"""

def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    else:
        return False
print(large_power(2, 13)) #Should print true

print(large_power(2, 12)) #Should print false