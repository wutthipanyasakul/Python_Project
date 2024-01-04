# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 06:41:19 2024

@author: satha
"""

def username_generator(first_name, last_name):

    if (len(first_name) < 3 or len(last_name) < 4):
        user_name = first_name + last_name
    else:
        user_name = first_name[:3] + last_name[:4]
    return user_name    

print(username_generator("Abe", "Simpson"))

def password_generator(user_name):
  password = ""
  last_letter = user_name[-1]
  length = len(user_name)-1
  for char in user_name:
    password = last_letter + user_name[0:length]
  return password

print(password_generator("Peter"))