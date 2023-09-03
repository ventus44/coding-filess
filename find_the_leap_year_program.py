def is_leap_year(year):
#this checks if the leap year is dividable by 4
    if year % 4 == 0:
#here it check if the year is also dividable by 100 if it is the function moves to the next condition
        if year % 100 == 0:
#here it check if the year is dividable by 400 if it is thes it's a leap year, if not it's not a leap year
            if year % 400 == 0:
                print("Leap Year")
#the else statement handles the situation that the year is not divisible by either of the numbers above
            else:
                print("Not leap year")
        else:
           print("leap year")
    else:
        print("Not leap year")
#here we basically put whatever year we want to check
is_leap_year(2007)