"""
set up function fib with argument n:
    if n is equal to 1:
        print 1
    elif n>1:
        print the first two terms manually
        initialise a at 0
        initialise b at 1
        for i in range 2 to n:
            assign b to b plus a
            assign a to b
            print b
            
prompt user to enter number
if number less than or equal to zero:
    print statement notifying user to enter a positive integer
else:
    print the number of terms by calling the function and inputting the number entered
"""

def fib(n):   
    if n==1:
        print(0)
        
    elif n>1:
        print("0","\n"+"1")
        a = 0
        b = 1
        for i in range(2,n):
            b,a = b+a,b
            print(b) 
            
            
number = int(input("please enter a non negative integer here:"))
if number <= 0:
   print("Plese enter a positive integer")
else:
   print("the following are the first",number,"terms of the fibonacci series:")
   fib(number)
       
       