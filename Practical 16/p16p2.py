"""
set up function with two arguments:
    assign empty variable to divisors
    for i in range 1 to the minimum of the two arguments plus one:
        if the first argument is perfectly divisible by i and
        if the second argument is perfectly divisible by i:
            add i to the tuple divisors 
        return the variable divisors

prompt the user to input a number
prompt the user to input a number
if either the first or second number are less than or equal to zero:
    print error message 
else:
    call the function with the two numbers inputted
    print the common divisors 
    
    initalise a total value at zero
    for d in divisiors:
        add d to the total for each iteration 
    print the sum of the common divisors

"""


def findDiv(num1, num2):
    """
    

    Parameters
    ----------
    num1 : positive integer
    num2 : positive integer

    Returns
    -------
    divisors : numbers that are factors of both num1 and num 2

    """
    divisors =()
    for i in range(1, min(num1,num2)+1):
        if num1 %i == 0 and num2 %i ==0:
            divisors += (i,)
    return divisors

number1 = int(input("enter a positive integer:"))
number2 = int(input("enter another psoitive integer here:"))
print( "\n")
if number1 <= 0 or number2 <=0:
    print("numbers shoulf be greater than 0")
else:
    divisors = findDiv(number1,number2)
    print("the common divisors of", number1, "and", number2, "are:", divisors)
    
    total = 0
    for d in divisors:
        total += d
    print("sum of the common divisors is:", total)
    


        
