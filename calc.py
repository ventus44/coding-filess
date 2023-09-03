#we define functions add sub mult div
#we return the action
#then we print a str data type that follow through the action
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n" )

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n" )

def mult(a, b):
    answer = a * b
    print(str(a) +  " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
#this is a while loop that run the program infinite times until we tell it to stop
while True:
#this line basically prints our options acording to the letter of  the alphabet
    print("A. Addition")
    print("B.Subtraction")
    print("C.multiplication")
    print("D.division")
#this is a line that prompts us to input our choice 
    choice = input("input your choice: ")
#here the loop calculates and sees the choices 
#after it sees our choice it promps us to input the two numbers that we will run a calculation on
#it then executes the claclulation
    if choice == "a" or choice =="A":
       print("Addition")
       a = int(input("first number: "))
       b = int(input("second number: "))
       add(a, b)
    elif choice =="b" or choice =="B":
       print("Subtraction")
       a = int(input("first number: "))
       b = int(input("second number: "))
       sub(a, b)
    elif choice =="c" or choice =="C":
        print("multiplication")
        a = int(input("first number: "))
        b = int(input("second number: "))
        mult(a, b)
    elif choice =="d" or choice =="D":
        print("division")
        a = int(input("first number: "))
        b = int(input("second number: "))
        div(a, b)
    elif choice=="e" or choice=="E":
        print("program ended")
#this line is enabling us to quit the program         
    exit()
            


