"""
set up the function with argument x:
    for x in range (1 to x+1):
        initate the sum total at zero
        for i in range 1 to x minus one :
            if x is exactly divisible by i:
                add i to the sum total
        if the sum total equal x:
            print out the value of x for which this holds
            

prompt the user to enter a number
if the number is greater than or equal to zero:
    call the function with the number entered as input 
else:
    print that a positive integer must be entered
  """  

def findPerf(x):
    """
    

    Parameters
    ----------
    x : is a positive integer
        
    Returns
    -------
    None.

    """
    for x in range(1, x+1):
        total = 0
        for i in range(1, x-1):
            if(x % i == 0):
                total = total + i    
                
        if(total == x):
            print(x)
            
number = int(input("please neter a positive integer here:"))
if number>=0:        
    print("the perfect number up to and including", number,"are:")
    findPerf(number)
else:
    print("please enter a positive integer")

