# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 04:20:14 2024

@author: satha
"""

#challenges: control flow 2

#Check if we are over our budget

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500


# Calculate the total amount of expenses

total = food_bill + electricity_bill + internet_bill + rent


# Check if the total is greater than the budget and store the result in over_budget
if total > budget:
    over_budget = True
else:
    over_budget = False

# Show the results

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))