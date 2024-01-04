# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 04:44:45 2024

@author: satha
"""

#challenges: control flow 5

#Divisible By Ten

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False