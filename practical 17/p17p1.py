"""
set up the function with one argument:
    initalise divisors tuple, including 1 and the input
    for i in range 2 to the input divided by 2 plus one:
        if input is perfectly divisible by i:
            add i to the divisors tuple
        return divisors
    
    
prompt the user to input a number

if the number entered is less than or equal to zero:
    print error message notifying user that number entered should be greater than zero
else:
    call the function with the number entered as input
    print the divisors
    
    sum the divisors using a for loop and counter
"""

def findDiv(num1):
    """


    Parameters
    ----------
    num1 : positive integer.

    Returns
    -------
    divisors: divisors of the input

    """
    
    divisors =(1,num1)
    for i in range(2, num1//2+1):
        if num1 %i == 0:
            divisors += (i,)
    return divisors

number1 = int(input("enter a positive integer:"))

print( "\n")
if number1 <= 0:
    print("numbers shoulf be greater than 0")
else:
    divisors = findDiv(number1)
    print("the divisors of", number1,  "are:", divisors)
    
    total = 0
    for d in divisors:
        total += d
    print("sum of the common divisors is:", total)
    


        