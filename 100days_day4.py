        # Radomisation and lists #

# import random

# random_integer = random.randint(5,10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# print(random_float*random_integer)



##Heads or Tails Generator

# import random

# option = random.randint(0,1)
# if option == 0:
#     print("Tails")
# else:
#     print("Heads")


## Lists(Banker Roulete)

# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(",")
# banker = names[random.randint(0,len(names)-1)]
# print(f"{banker} is going to buy the meal today!")



## Rock, Paper, Scissors
import random
import sys
from enum import Enum

class rps(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

player_choice = input("Enter \n1 for Rock\n2 for Paper\n3 for Scissors\n\n")
player = int(player_choice)
if player < 1 or player > 3:
    sys.exit("Enter a number between 1 and 3!")

computer_choice = random.choice("123")
computer = int(computer_choice)

print("You chose " + str(rps(player)).replace("rps.",""))
print("Computer chose " + str(rps(computer)).replace("rps.",""))

if player == 2 and computer == 1:
    print("You win")
elif player == 1 and computer == 3:
    print("You win")
elif player == 3 and computer == 2:
    print("You win")
elif player == computer:
    print("Tie Game!")
else:
    print("Computer wins")    













