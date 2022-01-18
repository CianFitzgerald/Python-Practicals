"""
set up function max wih two arguments a and b:
 if a is greater than b:
     return a
 else:
     return b
 
prompt user to enter number
prompt the user to enter another number
assign variable to the function created and input numbers entered by user
print out the largest number of the two i.e print the variable created above using the function
   """


def max(a,b):
    """
    

    Parameters
    ----------
    a : floating point number.
    b : floating point number.

    Returns
    -------
    TYPE
        returns the largest of the two numbers.

    """
    if a>b:
        return a
    else:
        return b
    
numb1 = float(input("enter a number:"))
numb2 = float(input("enter a number:"))
biggest = max(numb1, numb2)
print("the largest of", numb1, "and", numb2, "is", biggest)