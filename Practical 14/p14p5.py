"""
set up the function fib with one argument x:
    if x is less than or equal to 1:
        print x
        return x
    else:
        assign the formula for the fibonnaci sequence to a variable fib_series
        print fib_series
        return the variable fib_series


prompt the user to enter a number
while the number is greater than or equal to zero:
    print statement regarding the recursion
    assign an empty list to the variable L
    for number in range zero to the number entered:
        assign to a variable the function with the number entered as input
        append the empty list with this variable 
    print the list
    prompt the user to enter a new number
"""


def fib(x):
    """
    Parameters
    ----------
    x : must be an integer

    Returns
    -------
    returns the general formula of the fibonnaci sequence

    """

    if x<=1:
        print(x)
        return x
    else:
        fib_series = (fib(x-1)+fib(x-2))
        print(fib_series)
        return fib_series
    


number = int(input("please enter an integer here:"))
while number>=0:

    print("\n"+"The operation of the recursion towards the base case is as follows:")
    L = []
    for i in range(0,number):  
        newL = fib(i)
        L.append(newL)
    print("\n"+"The first",number, "terms of the series are:",L)
    number = int(input("please enter an integer here, enter a negative number to terminate:"))


