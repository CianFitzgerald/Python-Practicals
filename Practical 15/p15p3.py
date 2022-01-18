"""
set up the function series with one argument x:
    if x is equal to zero:
        print 13
        return 13
    if x is equal to one:
        print 8
        return 8
    else if x>1:
        assign the formula for the for the series to a variable rec
        print this variable
        return this variable 


prompt the user to enter a number
while the number is greater than or equal to zero:
    print statement regarding the recursion
    assign an empty list to the variable L
    for number in range one to the number entered plus one:
        assign to a variable the function with the number entered as input
        append the empty list with this variable 
    print the list
    prompt the user to enter a new number
"""


def series(x):
    """

    
    Parameters
    ----------
    x : integer greter than or equal to 0.

    Returns
    -------
     Returns the number of terms of the sequence and print statements for the operation of the recursion

    """
    if x ==0:
        print(13)
        return 13
    elif x==1:
        print(8)
        return 8
    elif x>1:
        a = series(x-2)+13*series(x-1)
        print (a)
        return a


number = int(input("please enter an integer here:"))
while number>=0:
    print("\n"+"The operation of the recursion towards the base case is as follows:")
    L = []
    for number in range(number):  
        newL = series(number)
        L.append(newL)
    print("\n"+"The first", number, "terms of the series are:",L)
    number = int(input("please enter an integer here, enter a negative number to terminate:"))


