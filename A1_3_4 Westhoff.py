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
