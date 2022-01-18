'''
PSEUDOCODE:
    
prompt user for input (2 numbers)
if sum of number is greater than 100:
    program prints "that is a big number"
'''   


print("when prompted, enter two numbers.")
number1 = int(input("enter first number here:"))
number2 = int(input("enter second numbers here:"))
total = number1 + number2
if total > 100:
    print("That is a big number!")
    
