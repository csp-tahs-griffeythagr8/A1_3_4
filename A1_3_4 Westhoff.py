"""
A1_3_4 Westhoff.py
Programmer: Reece Westhoff
"""

#Place Your Code Below
#I will read the repository ReadMe
#I will update document with my own code
usr_input = input()
try:
  sani_input = int(usr_input)
  print("Is an integer")
except(TypeError, ValueError):
  print("Not an integer")
