#this line defines the main function
def main():
#this line converts the dollars to pounds 
    convert_to_pounds = lambda dollars: dollars * 0.78
#this line basically explains what the progam does
    print("This program converts US dollars to pounds Sterling")
    print()
#this line is used to convert the users input into a floating number
    dollars = float(input("Enter your amount in dollars: ")) 
#this line applies the lambda function and does the conversion
    pounds = convert_to_pounds(dollars)
#this line prints the conversion
    print("This is", pounds, "pounds.")
#we finally call main
main()
