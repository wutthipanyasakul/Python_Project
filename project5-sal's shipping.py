# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:08:02 2023

@author: satha
"""

#Sal's Shipping

"""
Instrunctions:
    
Build a program that will take the weight of a package and determine the cheapest way 
to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight 
is triple the rate of ground shipping.
"""

#Project Starts

#Ground Shipping:

weight = 20

if weight <= 2:
    
    cost = (1.50 * weight) + 20
    
    print(f'Shipping cost is: $ {cost}.')

elif weight > 2 and weight <= 6:
    cost = (3 * weight) + 20
    print(f'Shipping cost is: $ {cost}.')

elif weight > 6 and weight <= 10:
    cost = (4 * weight) +20
    print(f'Shipping cost is: $ {cost}.')
    
elif weight > 10:
    cost = (4.75 * weight) + 20
    print(f'Shipping cost is: $ {cost}.')
    
else:
    print("Invalid input")    

#Ground Shipping Premium:
    
premium_cost = 125

print(f'The premium shipping cost is: ${premium_cost}.')

#Drone Shipping

if weight <= 2 :
    
    cost = 4.5 * weight
    print(f'The Drone shipping cost is:  ${cost}.')
    
elif weight > 2 and weight <= 6:
    cost = 9 * weight
    print(f'The Drone shipping cost is: ${cost}.')

elif weight > 6 and weight <= 10:
    cost = 12 * weight
    print(f'The Drone shipping cost is: ${cost}.')
elif weight > 10 :
    cost = 14.25 * weight
    print(f'The Drone shipping cost is: ${cost}.')
else:
    print('Invalide input.')
    