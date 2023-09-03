import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Chose rock, paper, scissors, or exit: ")
    
    if user_input == "exit":
        print("game ended")
        print("You have a total score of: " + str(user_points) + " and the computer total score is: " + str(computer_points))
        exit = True
        continue

    computer_input = random.choice(options)

    if user_input == "rock":
        if computer_input == "rock":
            print("You picked rock")
            print("Computer picked rock")
            print("it's a tie")
        elif computer_input == "paper":
            print("You picked rock")
            print("Computer picked paper")
            print("computer wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("You picked rock")
            print("Computer picked scissors")
            print("you win")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("You picked paper")
            print("Computer picked rock")
            print("You win")
            user_points += 1
        elif computer_input == "paper":
            print("You picked paper")
            print("Computer picked paper")
            print("It's a tie")
        elif computer_input == "scissors":
            print("You picked paper")
            print("Computer picked scissors")
            print("computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("You picked scissors")
            print("Computer picked rock")
            print("You lose")
            computer_points += 1
        elif computer_input == "paper":
            print("You picked scissors")
            print("Computer picked paper")
            print("You win")
            user_points += 1
        elif computer_input == "scissors":
            print("You picked scissors")
            print("Computer picked scissors")
            print("It's a tie")

    elif user_input != "rock" and user_input != "paper" and user_input != "scissors":
        print("invalid input")
