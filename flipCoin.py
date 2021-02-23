# This is a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 
# This program generates a random number, either 0 or 1. Then use that number to print out Heads or Tails.

import random 

# Psuedocode
# Calculate a random number and save it into a variable (Round it). 
# If the random number is 1, print heads.
# If the random number is 0, print tails. 

def flipCoin():
    random_number = round(random.random())
    if random_number == 1:
        print("Heads")
    else:
        print("Tails")

flipCoin()
