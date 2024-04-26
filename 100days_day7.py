### Function with inputs ###

## Simple function

# def greet():
#     print('Hello there')
#     print('How are you?')
#     print('How\'s the weather today?')
# greet()

## Function that allows input

# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'How are you {name}?')
# greet_with_name("Beeka Arnold")   

## Functions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How is {location}") 
# greet_with("Arnold Beeka", "Kampala")    

## Functions with keyword arguments

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How is {location}") 
# greet_with(name = "Arnold Beeka", location = "Kampala")
    
## Paint Area calculation exercise

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# def paint_calc(height=test_h, width=test_w, cover=coverage):
#     number_of_cans = round((height * width)/cover)
#     print(f"You'll need {str(number_of_cans)} cans") 
# paint_calc(test_h,test_w,coverage)    

## Prime number checker

def prime_checker(number):
	is_prime = True
	for i in range(2,number):
		
		if number%i == 0:
			is_prime = False
	if is_prime:
		print("It's a prime number")
	else:
		print("It's not a prime number")	
		

n = int(input("Check this number: "))   
prime_checker(number=n)





    
