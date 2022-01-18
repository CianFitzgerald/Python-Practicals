'''
prompt the user to enter a number
while the number entered is greater than or equal to zero:
    initiate the sum at zero
    for i in the range one to (number entered plus one):
        sum is equal to the sum plus i 
    print the sum of the integers
    
    prompt the user to enter another number, 
    notifying them that the program will terminate
    if a negative number is entered
'''


number = int(input("please eneter a positive integer here:"))
print("number entered is:", number)
while number>=0:
    sum = 0
    for i in range (1, number+1):
        sum += i
    print("sum of first " , number, "numbers is:", sum)
    number = int(input("please eneter a positive integer here, enter a negative number to terminate the program:"))

        
        
            
 
