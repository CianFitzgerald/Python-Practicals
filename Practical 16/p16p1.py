"""
set up the function series with one argument x:
    if x is equal to 1:
        print 2
        return 2
    else if x>1:
        assign the formula for the for the series to a variable rec
        print this variable
        return this variable 


prompt the user to enter a number
while the number is greater than or equal to one:
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
    x : integer greater than or equal to 1.

    Returns
    -------
    Returns the number of terms of the sequence and print statements for the operation of the recursion

    """
    if x ==1:
        print(2)
        return 2
    elif x>1:
        rec = 2*series(x-1)
        print (rec)
        return rec
    
    
number = int(input("please enter an integer here:"))

while number>=1:
    print("\n"+"The operation of the recursion towards the base case is as follows:")
    L = []
    for number in range(1, number+1):  
        newL = series(number)
        L.append(newL)
    print("\n"+"The first", number, "terms of the series are:",L)
    number = int(input("please enter an integer here, enter zero or a negative number to terminate:"))



    