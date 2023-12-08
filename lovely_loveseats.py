#Project 2

#Project's Name: : Receipts for Lovely Loveseats

#This projects is comprised of two sections and 17 steps

#Section 1 : Adding In The Catalog

#First Step: Create a lovely loveseat description

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#Second Step: Create a price for the loveseat

lovely_loveseat_price = 254.00

# 3rd step: Create a style description variable

stylish_settee_description ="Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#4th step: Create a price for Stylish Settee.

stylish_settee_price = 180.50

#5th Step: Create Luxurious lamp description

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

#6th Step: Create a price for the Luxurios lamp

luxurious_lamp_price = 52.15

#7th Step: Create a variable for sale tax

sales_tax = 0.088

#Section 2: Our First Customer

# 8th Step: Create a running tally of our customers' expenses

customer_one_total = 0

#9th Step: Create a list of description of things our customers are purchasing

customer_one_itemization= " "

#10th Step: Add the price to the running tally

customer_one_total += lovely_loveseat_price

#11th Step: Add the item our customers are purchasing in their basket

customer_one_itemization += "1.Lovely Loveseat "

#12th Step: Add another price to the running tally

customer_one_total += luxurious_lamp_price

#13th Step: Add another item our customers are purchasing in their basket


customer_one_itemization += "2.Luxurious lamps"

#14th Step: Calculate Sale Tax

customer_one_tax = customer_one_total * sales_tax

#15th Step: Add a new sale tax to our customer's total cost

customer_one_total += customer_one_tax

#16th Step: print out our customer's receipt by starting with their itemization

print("Customer One Items: " , customer_one_itemization)

#17th Step: print out our customer's total cost

print("Customer One Total: ", customer_one_total)








