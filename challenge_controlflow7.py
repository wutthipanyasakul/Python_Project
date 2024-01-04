# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 04:46:54 2024

@author: satha
"""

#challenges: control flow 7

#Same Name

"""
- Define the function to accept two strings, your_name and my_name
- Test if the two strings are equal
- Return True if they are equal, otherwise return False

"""

def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else: 
        return False

print(same_name("Colby", "Colby"))
# should print True

print(same_name("Tina", "Amber"))
# should print False

