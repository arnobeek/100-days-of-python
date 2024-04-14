                 # Control Flow#

# print("Welcome to the Rollercoaster.")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride.")
# else:
#     print("You are not tall enough to ride! ")  



##Odd or Even number challenge

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("The number is Even.")
# else:
#     print("The number is Odd.")    



## Rollercoaster Ticketing project
print("Welcome to the rollercoaster.")
height = int(input("What is your height in cm? "))
total_bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you? "))
    take_pic = input("Do you want to take a pic? Y or N").upper()
    if age > 18:
        total_bill += 12
        if take_pic == "Y":
            total_bill += 3
        print(f"Your total bill is ${total_bill}")
    elif age > 12:
        total_bill += 7
        if take_pic == "Y":
            total_bill += 3

    elif age < 12:
        total_bill += 5
        if take_pic == "Y":
            total_bill += 3
        print(f"Your total bill is ${total_bill}")    

else:
    print("You are not tall enough to ride.")   





## BMI Calculator project
# height = float(input("What is your height in m? "))
# weight = float(input("What is your weight in kg? "))
# bmi = round(weight/height**2,2)
# if bmi > 35:
#     print(f"Your bmi is {bmi}, you are clinically obese.")
# elif bmi > 30:
#     print(f"Your bmi is {bmi}, you are obese.")
# elif bmi > 25:
#     print(f"Your bmi is {bmi}, you are overweight.")
# elif bmi > 18.5:
#     print(f"Your bmi is {bmi}, you have a normal weight.") 
# else:
#     print(f"Your bmi is {bmi}, you are underweight.")           




## Leap Year Checker
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a Leap year.")                        
#     else:
#         print("Is a Leap year.")       
# else:
#     print("Not a Leap year.")    




   