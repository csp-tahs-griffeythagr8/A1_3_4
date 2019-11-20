"""
A1_3_4 #A1_3_4 Stainbrook.py
Programmer: Ethan S
"""
usr_input = input()
import random
guess = 23
def hiLo_game(guess):
    rand_num = random(1,100)
    if guess == rand_num:
        print ("Yes! You got it right!")
    else:
        if guess < rand_num:
            print ('Your guess was too low. Try again!')
        else:
            print ("Your guess was too high! Try again!")
    try:
        sani_input = int(usr_input)
        print("Is an integer")
    except(TypeError, ValueError):
        print("Not an integer")
