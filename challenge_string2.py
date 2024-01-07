# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:40:33 2024

@author: satha
"""

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#split highlighted_poems at the commas and saving it to highlighted_poems_list

highlighted_poems_list = highlighted_poems.split(",")

#iterate through highlighted_poems_list using a for loop and 
#for each poem strip away the whitespace and append it to your new list

highlighted_poems_stripped = []

for element in highlighted_poems_list:
  element = element.strip(" ")
  highlighted_poems_stripped.append(element)

#Iterate through highlighted_poems_stripped and split each string around the : characters 
#and append the new lists

highlighted_poems_details = [item.split(':') for item in highlighted_poems_stripped]


#Iterate through highlighted_poems_details and 
#for each list in the list append the appropriate elements into the lists titles, poets, and dates

titles = []
poets = []
dates = []




for item in highlighted_poems_details:
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])
print(titles)
print(poets)
print(dates)

#write a for loop that uses .format() to print out the following string for each poem

for item in highlighted_poems_details:
  title=item[0]
  poet=item[1]
  date=item[2]
  message = "The poem {} was published by {} in {}."
  print(message.format(title, poet, date))