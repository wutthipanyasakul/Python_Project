# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 06:01:26 2024

@author: satha
"""

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Splitting the authors string into a list and then extracting the last names
author_last_names = [name.split()[-1] for name in authors.split(",")]

print(author_last_names)
