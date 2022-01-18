'''
note: first two terms must be input manually as they are not a part of the general formula 
for the fibonacci series

prompt user to enter a number
if number is equal to zero:
    print an error, notifying that a positive integer must be entered.
else if number is equal to one:
    print that the first term is zero
else if number is greater than one: 
    print statement regarding number of terms to be printed
    print first two terms manually, see note above
    asign a a value of 0
    assign b a value of 1 
    and assign i a value of 3 
    while i is less than or equal to number 
        asign b to b+a
        assign a to b
        increase i by one
        print b
'''


number = int(input("enter a positive integer here:"))
print("the number you have entered is:", number, "\n")
if number == 0:
    print("Error: please enter a positive integer to calculate that number of terms of the fibonacci series")
elif number==1:
    print("the following is the first term of the fibonacci series:", "\n", "0")
elif number >1:   
    print("the following are the first",number,"terms of the fibonacci series:")
    print("0","\n"+"1")
    a,b,i = 0,1,3
    while i <= number:
        b,a = b+a,b
        i += 1 
        print(b)



