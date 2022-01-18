'''
prompt the user to input a number
if the number is equal to zero:
    print statement notifying that number must be greater than or equal to one
else if number is one:
    print the first number of the catalan numbers
else if number greater than one:
    print statement regarding number of terms to be printed
    initiate Cn at 1 
    for n in range 0 to number minus one:
        assign catalan the equation of the formula for the Cn+1 term
        assign Cn to Catalan
        print the corresponding statements 
        '''


number = int(input("Please enter an integer here:"))
if number == 0:
    print("please enter a number greater than or equal to one  calculate that number of catalan numbers")
elif number == 1:
    print("the following are the first",number,"terms of the catalan numbers:", "\n"+"1")
elif number>1:
    print("the following are the first",number,"terms of the catalan numbers:", "\n"+"1")
    C_n = 1
    for n in range(0,number-1):
        catalan = ((2*(2*n+1))*C_n)/(n+2)
        C_n = catalan
        print(int(catalan)) 
        

