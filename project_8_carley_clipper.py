# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 22:45:50 2024

@author: satha
"""

#Project 8: Carly's Clippers
"""
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.
"""
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Prices and Cuts:
total_price = 0

#Find Total price
for price in prices:
  total_price += price

#Find average total price
average_price = total_price / len(prices)

print(f"Average Haircut Price: {average_price}")

new_prices = [price - 5 for price in prices]

print(new_prices)

#Revenue

total_revenue = 0
hairstyles_amount = len(hairstyles)
#Find total revenue
for i in range(hairstyles_amount):
  total_revenue += (prices[i] * last_week[i])
print(f"Total Revenue: {total_revenue}")

#Find average daily revenue
average_daily_revenue = total_revenue / 7

#Hairstyle under 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i] <30 ]

print(cuts_under_30)
