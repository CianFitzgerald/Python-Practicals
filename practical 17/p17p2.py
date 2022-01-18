"""
set up the function with two arguments:
    initalise divisors tuple, including 1 
    for i in range 2 to the maximium of the two arguments divided by 2:
        if both arguments are perfectly divisible by i:
            add i to the divisors tuple
        return divisors
    
    
prompt the user to input a number
prompt the user to input another number

if either number entered is less than or equal to zero:
    print error message notifying user that numbers entered should be greater than zero
else:
    call the function with the numbers entered as input
    print the divisors
    
    sum the divisors using a for loop and counter
"""



def findDiv(num1,num2):
    divisors =(1,)
    for i in range(2, max(num1//2, num2//2)+1):
        if num1 %i == 0 and num2 %i ==0:
            divisors += (i,)
    return divisors

number1 = int(input("enter a positive integer:"))
number2 = int(input("enter a positive integer:"))


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
    


        