"""
set up function max wih two arguments a and b:
 if a is greater than b:
     return a
 else:
     return b
 
prompt user to enter number
prompt the user to enter another number
print the largest of the two numbers by entering the function directly into the print statement 
"""

def max(a,b):
    """
    

    Parameters
    ----------
    a : floating point number.
    b : floating point number.

    Returns
    -------
    returns the largest of the two numbers.


    """
    if a>b:
        return a
    else:
        return b
    
numb1 = float(input("enter a number:"))
numb2 = float(input("enter a number:"))

print("the largest of", numb1, "and", numb2, "is", max(numb1,numb2))