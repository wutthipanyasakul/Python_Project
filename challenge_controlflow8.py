# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 04:50:22 2024

@author: satha
"""

#challenges: control flow 8

#Always False

"""
- Define the function to accept a single parameter called num
- Use a combination of <, > and and to create a contradiction in an if statement.
- If the condition is true, return True, otherwise return False. 
The trick here is that because we’ve written a contradiction, the condition should never be true, 
so we should expect to always return False.
"""
def always_false(num):
    if (num > 1 and num < 1):
        return True
    else:
        return False

print(always_false(0))
# should print False

print(always_false(-1))
# should print False

print(always_false(1))
# should print False
