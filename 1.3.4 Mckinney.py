'''
1.3.3
Connor Mckinney
'''
import random
guess= 47
def hiLo_game(guess):
    rand_num = 788
    if guess == rand_num:
        print ("Congrats you got it right")
    elif guess > rand_num:
        print ("your number is too high")
    else:
        print ("your number is too low")
