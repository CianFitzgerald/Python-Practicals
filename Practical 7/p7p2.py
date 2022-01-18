'''
PSEUDOCODE:
    
prompt user to input year
if year is not exactly divisible by 4 then it is a common year
elseif year is not exactly divisible by 100 then it is a leap year
elseif year is not exactly divisible by 400 then it is a common year
else it is a leap year

'''




year = int(input("Enter a year:"))
print("Year entered:", year)

if(year % 4 != 0):
    print(year, "is a common year")
        
elif (year % 100 !=0):
    print(year, "is a leap year")
        
elif (year % 400 != 0):
    print(year, "is a common year.")
    
else:
    print(year, "is a leap year")
        
