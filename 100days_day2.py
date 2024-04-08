# Data types
# digits = input("Type a two digit number: ")
# digit1 = int(digits[0])
# digit2 = int(digits[1])
# print(digit1 + digit2)

# BMI Calculator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# heigh_t = float(height)
# weigh_t = int(weight)
# bmi = weigh_t/heigh_t**2
# print(f"You're BMI is {bmi}")

# Life in weeks
# age = int(input("How old are you? "))
# years = 90-age
# months = years*12
# weeks = years*52
# days = years*365
# print(f"You have {days} days, {weeks} weeks and {months} months left")




# Tip Calculator
print("Welcome to the Tip Calculator!")
bill = int(input('What was the total bill? '))
customers = int(input('How many people to split the bill? '))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
if tip == 10:
    total_bill = (bill/customers)*1.10
elif tip == 12:
    total_bill = (bill/customers)*1.12
else:
    total_bill = (bill/customers)*1.15    



print(f'Each customer should pay: {round(total_bill,2)}')
