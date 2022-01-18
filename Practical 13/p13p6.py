"""
set up function fact with argument x:
    if x is equal to zero:
        return 1
    else:
        assign fac to x multiplied by the function fact with variable x minus one
        print fac
        return fac
    
prompt the user to enter a number 
if the number is greater than or equal to zero:
    print the factorial of the number using the fact function with the users input as the variable 
else:
    notify the user that they have netered a negative integer and to try again
"""


def fact(x):
    """
    

    Parameters
    ----------
    x : the number for which you would like to find the factorial.

    Returns
    -------
    returns the factorial of the number x.

    """
    if x==0:
        return 1
    else:
        fac = x*fact(x-1)
        print(fac)
        return fac

 
number = int(input("please enter a number here"))
if number>=0:
    print("the factorial of", number, "is", fact(number))
else:
    print(number, "is a negative integer, please try again")
    
    
