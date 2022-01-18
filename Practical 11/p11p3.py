'''
note: first two terms must be input manually as they are not a part of the general formula 
for the fibonacci series

prompt user to enter a number
while the number entered is greater than or equal to zero:   
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
        for i in range 2 to the number entered
            asign b to b+a
            assign a to b
            print b
        prmopt user for another number, notifying them that a negative number will terminate the program
'''



number = int(input("please enter a number here:"))
print("The number you have entered is:", number, "\n")
while number>=0:
    if number == 0:
        print("Error: please enter a positive integer to calculate that number of terms of the fibonacci series") 
        break
    elif number==1:
        print("the following is the first term of the fibonacci series:", "\n" + "0")
        break
    else:
        print("the following are the first",number,"terms of the fibonacci series:")
        print("0","\n"+"1")
        a = 0
        b = 1
        for i in range(2,number):
            b,a = b+a,b
            print(b) 
        number = int(input("please enter a number here, enter a negative number to exit:"))