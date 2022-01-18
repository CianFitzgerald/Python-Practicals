'''
prompt the user to enter a positive integer 
while number entered is greater than or equal to zero:
    if the number is equal to zero:
        set factorial equal to one 
        print the number entered and its associated factorial
        prompt the user to enter another integer 
    else:
        initiate the factorial at one 
        intiate the counter at one
        while the count is less than the number entered:
            factorial is equal to itself multiplied ny the count 
            increase the count by one 
        print the number entered and its associated factorial
    prompt the user to enter another number, 
    notifying them that the program will terminate
    if a negative number is entered
'''


number = int(input("please enter a positive integer here:"))
while number>=0: 
   if number==0:
        factorial = 1
        print("factorial of" , number, "numbers is:", factorial)   
        number = int(input("please eneter a positive integer here, if number is negative the program will terminate:"))
   else:
       factorial = 1
       count = 1
       while count<=number:
           factorial *= count
           count +=1
       print("factorial of" , number, "numbers is:", factorial)
       number = int(input("please eneter a positive integer here, if number is negative the program will terminate:"))
        
