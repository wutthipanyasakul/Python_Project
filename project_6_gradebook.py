# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 02:29:49 2023

@author: satha
"""

#Project 6: Gradebook

"""
Instructions:
    
You are a student and you are trying to organize your subjects and grades using Python. 
Let’s explore what we’ve learned about lists to organize your subjects and scores.

"""

#Program starts

#Create Some Lists:

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

last_semester_gradebook = [['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65]]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

#Add More Subjects:

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

#Modify The Gradebook:

gradebook[-1][-1] = 98 

#poetry_score = gradebook[2]

#poetry_score.remove(poetry_score[1])

gradebook[2].remove(gradebook[2][1])

gradebook[2].append("Pass")

#One Big Gradebook!

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)










