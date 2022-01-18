'''
prompt the user to enter a number
if the number is less than zero:
    print an error, that the number was less than zero
else:
    initiate factorial at 1
    for i in range 1 to number entered plus one:
        set the factorial equal to itself multiplied by i
print the factorial of the number entered
'''

number = int(input("enter a number here for which you would like to find the factorial:"))
if number < 0:
    print("error, number entered was less than 0")
else:
    fact = 1
    for i in range(1,number+1):
        fact *= i
print("factorial of", number, "is", fact)

