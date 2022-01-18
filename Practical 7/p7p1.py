'''
PSEUDOCODE:
    
Prompt user for a year 
If the year is greater than 0:
    if the year entered is:exactly divisible by 4 and not exactly divisible by 100 or exactly divisible by 400 
        Then the year entered is a leap year
    else
        The year is a common year
else print that the year must be greater than zero 
                     


'''

year = int(input("Enter a year:"))
print("Year entered:", year)
if year>=0:
    if(year % 4 == 0 and year % 100 !=0)  or year % 400 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
else:
    print("year must be greater than zero.")
    