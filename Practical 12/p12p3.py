"""
set up the function with two arguments x (number) and y (tolerance):
    initiate i at 0
    while the absolute value of x minus i squares is greater than or equal to the tolerance 
    and i is less than or equal to x:
        assign i the value of i plus the tolerance squared
    if the absolute value of x minus i squared is less than y:
        return i
    
prompt user to input the number for which they would like to find the square root
prompt the user the tolerance they would liek 
if the number enetered is less than or equal to zero:
    print that a non negative number must be entered
else:
    print the approximate square root using the function
"""


def square(x,y):
    i = 0
    while abs(x-i**2)>=y and i<=x:
        i+=y**2
    if abs(x-i**2)<y:
        return i
        
number = float(input("please enter a floating point number for which you would like to find the square root"))
tolerance = float(input("please enter the tolerance with which you would like the approximation"))
if number <= 0:
   print("Plese enter a non negative floating point number")
else:
   print("approximate square root:", square(number, tolerance))
