'''
prompt the user for a number
initiate the factorial value at 1
set up for loop with range one to (number entered plus one):
    set the factorial equal to itself multiplied by the range i
print the final factorial
'''


number = int(input("please eneter a positive integer here:"))
print("number entered is:", number)
fact = 1
for i in range (1, number+1 , 1):
    fact *= i
print("factorial of" , number,"is", fact)  

        
        
 
