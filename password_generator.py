#we import the string library so we can manipulate strings
import string
#we import the random library so we can add the random element
import random
#in this line we add a list of ascii character to our code 
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
#we then define the function password 
def generate_password():
#here we ask the user how long does he want our password to be 
    password_length = int(input("How long do you want your password to be? "))
#here we shuffle the list of ascii characters
    random.shuffle(characters)
#this is created to hold all the character of the randomly generated password
    password = []
#this is a loop that runs as many times as the user wants it to 
    for x in range(password_length):
#this line add characters from our list
        password.append(random.choice(characters))
#this line does a suffle on the letters of the password
    random.shuffle(password)
#this line joins all the characters of the password into a single string with no spaces
    password = "".join(password)
#the new password is printed
    print(password)

#this line asks you if you want to print the new password
option = input("Do you want to generate a password? Yes or No: ")
#if the option is yes the program runs and it generates a password    
if option == "Yes":
    generate_password()
#if the answer is no the program ends 
elif option == "No":
    print("Program ended")
    quit()
#also if the input is invalid the program stops
else:
    print("Invalid input please input Yes or No")
    quit()

