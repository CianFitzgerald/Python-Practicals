"""
set up a function fact with variable x:
    initate the factorial value at 1
    set up for loop with range 1 to x+1:
        assign the factorial a value of itself muliplied the range i
    return the value of the factorial 

prompt the user to input a number 
if the nunber is greater than or equal to zero:
    print the number entered and it's factorial using the function 
else:
    print that the number entered must be a non negative integer.
    
"""


def fact(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res
    
number = int(input("please enter a number here"))
if number >= 0:
    print("the factorial of", number, "is", fact(number))
else:
    print("a non-negative integer must be entered")
