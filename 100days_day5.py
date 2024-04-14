                ## Loops ##


# fruits = ['Apple','Banana','Peach']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + 'Pie')



##Average students heights

# students_heights = input("Input a list of student heights ").split()
# for n in range(0, len(students_heights)):
#     students_heights[n] = int(students_heights[n])
# print(students_heights)

# total_height = 0
# for height in students_heights:
#     total_height += height
# print(total_height) 

# number = 0
# for student in students_heights:
#     number += 1
# print(number)    

# average_height = round(total_height/number)
# print(average_height)




##High Score Assignment

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)    

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score is: {highest_score}")        




##Range function(Adding numbers 1 to 100)

# total = 0
# for number in range(1,101):
#     total += number
# print(total)    




##Adding Evens

# total = 0
# for even in range(0,101,2):
#     total+=even
# print(total)   




## Fizz Buzz Challenge

# for number in range(1, 101):
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")        
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)   




## Python Password Generator

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters do you want in your password? \n"))
num_numbers = int(input("How many numbers would you like? \n"))
num_symbols = int(input("How many symbols would you like? \n"))

# Easy way
# password = ''
# for char in range(1, num_letters + 1):
#     rand_char = random.choice(letters)
#     password += rand_char

# for num in range(1, num_numbers+1):
#     rand_num = random.choice(numbers)
#     password+=rand_num

# for sym in range(1, num_symbols+1):
#     rand_sym = random.choice(symbols)
#     password += rand_sym
# print(password)

# Hard way
# password = []
# for char in range(1, num_letters + 1):
#     rand_char = random.choice(letters)
#     password += rand_char

# for num in range(1, num_numbers+1):
#     rand_num = random.choice(numbers)
#     password+=rand_num

# for sym in range(1, num_symbols+1):
#     rand_sym = random.choice(symbols)
#     password += rand_sym

# random.shuffle(password)
# pass_w = ''
# for i in password:
#     pass_w+=i
# print(pass_w)    



