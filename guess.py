# Write your code here :-)
from random import randint

played = True

while played:
    user = int(input("enter rock=0, paper=1, or scissor=2:"))
    guess = randint(0, 2)
    print("AI=", guess)

    if user == guess:
        print("equal")
    elif (
        (user == 0 and guess == 1)
        or (user == 1 and guess == 2)
        or (user == 2 and guess == 0)
    ):
        print("you lost")
    elif (
        (user == 0 and guess == 2)
        or (user == 1 and guess == 0)
        or (user == 2 and guess == 1)
    ):
        print("you win")
    else:
        print("Invalid")
    user_input = input("Continue (y/n)?")
    played = (False, True)[user_input == "y"]
