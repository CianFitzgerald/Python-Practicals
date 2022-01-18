
"""
PSEUDOCODE:
    
prompt user for input (3 numbers)
if number 1 is not exactly divisible by 2 and number 1 is greater than number 1 and number 2:
    print number 1 is largest odd number
else number 2 is not exactly divisible by 2 and number 2 is greater than number 1 and number 3:
    print number 2 is largest odd number
else number 3 is not exactly divisible by 2 and number 3 is greater than number 1 and number 2:
    print number 3 is largest odd number
else program prints that none of the numbers entered are odd.

""" 
     
number1 = int(input("enter a number here:"))
number2 = int(input("enter another number here:"))
number3 =int(input("finally, enter another number here:"))

if number1 % 2 != 0 and number1>(number2 and number3):
    print(number1, "is the largest odd number")
elif number2 % 2 != 0 and number2>(number1 and number3):
    print(number2 , "is the largest odd number")
elif number3 % 2 != 0 and number3>(number1 and number2):
    print(number3 , "is the largest odd number")
else:
    print("none of the numbers entered were odd, please try again")

