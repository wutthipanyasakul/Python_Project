# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 06:04:28 2024

@author: satha
"""

def common_letters(string_one, string_two):

    #Convert both strings to lower case if case-sensitivity is disired
    string_one = string_one.lower()
    string_two = string_two.lower()
    
    #Convert both string into set to avoid duplicates and for efficient loop
    
    set_one = set(string_one)
    set_two = set(string_two)
    
    #Find the intersection between the two
    
    common = set_one & set_two
    
    return sorted(list(common))
  
print(common_letters("banana", "cream"))

print(common_letters('python', 'ruby on rails'))