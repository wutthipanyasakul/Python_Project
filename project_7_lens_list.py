# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 05:15:40 2024

@author: satha
"""

#Project 7: Len's Slice

#Instruction:

""" You work at Len’s Slice, a new pizza joint in the neighborhood. 
    You are going to use your knowledge of Python lists to organize some of your sales data."""
    
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

#count the number of occurance of 2 in prices

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)


print(f'We sell {num_pizzas} different kinds of pizza!')

#pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices = list(zip(prices, toppings))
print(pizza_and_prices)

pizza_and_prices.sort()

print(pizza_and_prices)

#The cheapest pizza

cheapest_pizza = pizza_and_prices[0]

#The most expensive pizza

pricest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

pizza_and_prices.append([2.5,"peppers"])

print(pizza_and_prices)

#Three cheapest pizzas

three_cheapest = pizza_and_prices[0:3]

print(three_cheapest)





