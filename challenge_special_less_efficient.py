# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 06:14:49 2024

@author: satha
"""

def common_letters(string_one, string_two):
    
    #Convert both strings into lower case to avoid case-sensitivity
    string_one = string_one.lower()
    string_two = string_two.lower()
    
    #Initial an empty list to store common letters
    common =[]
    
    for letter in string_one:
        if letter in string_two and letter not in common:
            common.append(letter)
            
    return common
    
print(common_letters("banana", "cream"))  # Example usage
print(common_letters('python', 'ruby on rails'))  # Example usage