#!/usr/bin/python3
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
print("Welcome to my tip calculator")
bill = float(input("How much is the bill?\n $"))
tip = float(input("What percentage will the tip be?\n"))
people = int(input("How many people will split the bill?\n"))
tip = tip / 100
tip_percent = bill * tip
bill = bill + tip_percent
bill = bill / people
bill = round(bill, 2)
bill = "{:.2f}".format(bill)
print(f"Each person will pay ${bill}")