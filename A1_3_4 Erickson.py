"""
A1_3_2 Erickson.py
Programmer:Wyatt Erickson
"""
import random
guess = 12

def hiLo_game(guess):
    rand_num = random.randint(1,100)
    if guess == rand_num:
        print('congrats you found the correct number')
    elif guess < rand_num:
        print('this is too low')
    else guess > rand_num:
        print('this is too high')
