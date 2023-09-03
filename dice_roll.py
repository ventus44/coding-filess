import random

def roll_dice():
#this is a dcitionary that represents the shape of dice in letters art    
    DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
#this line asks the user for input if they want to roll the dice
    roll = input("Roll the dice ? (Yes/No): ")
#if they answer yes this while loop activates that rolls the dice randomly
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
#this line prints the result of the dice roll 
        print("dice rolled: {} and {}".format(dice1, dice2))
#this line joins the strings together with no spaces
        print("\n".join(DICE_ART[dice1]))
        print("\n".join(DICE_ART[dice2]))
#this line prompts the user for input and asks them if they want to roll the dice again 
 
        roll = input("Roll again? (Yes/No): ")
#this line calls the roll dice function
roll_dice()
