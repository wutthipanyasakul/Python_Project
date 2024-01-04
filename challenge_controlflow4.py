# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 04:35:18 2024

@author: satha
"""

#challenges: control flow 4

#Twice As Large

"""
Determine if one number is twice as large as another number
"""

def twice_as_large(num1, num2):
    if num1 > 2* num2:
        return True
    else:
        return False

print(twice_as_large(10, 5))
# should print False

print(twice_as_large(11, 5))
# should print True