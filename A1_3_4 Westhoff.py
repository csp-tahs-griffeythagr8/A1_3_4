"""
A1_3_4 Westhoff.py
Programmer: Reece Westhoff
"""

#Place Your Code Below
#I will read the repository ReadMe
#I will update document with my own code
import random
guess = 26
def hiLo_game(guess):
    rand_num = random.randint(1,100)
    if rand_num > guess:
        print ('Too low')
    if rand_num < guess:
        print ('Too high')
    if rand_num == guess:
        print ('Winner')
hiLo_game(guess)

usr_input = input()
try:
  sani_input = int(usr_input)
  print("Is an integer")
except(TypeError, ValueError):
  print("Not an integer")

"""
Code:
1. usr_input can either replace guess or you can use input instead of the programmer assigned value. 
2. Sanitizing your code should come directly after your guess variable. 
3. Whether using usr_input or guess you need to pull in user data to put into your function. Otherwise the game doesn't work as intended. 
"""
