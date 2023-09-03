#we create the main function
def main():
    print("This is monthly interest calculator: ")
    print("")

#we store in the principal variable the flot of the input
    principal = float(input("input the loan amount: "))
#we do the same for the interest rate 
    apr = float(input("input the annual interes rate: "))
#we also do the same for the amount of years 
    years = float(input("input the ammount of years: "))
#we calculate the monthly interest rate 
    monthly_interest_rate = apr / 1200
#we also calculate the amount of months    
    amount_of_months = years * 12
#and we also calculte the monthly payment
    monthly_payment = principal * monthly_interest_rate / (1 -(1 + monthly_interest_rate) ** (-amount_of_months))

#we print the monlthy payment for the loan and we exclude decimal 
    print("the monthly payment fo the loan is : %.2f "% monthly_payment)
#we finally call main
main()