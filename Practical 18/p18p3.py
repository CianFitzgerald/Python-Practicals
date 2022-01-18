"""
deine the word count function with argument x:
    initialize the count at zero
    for i in range zero to the length of x:
        this loop works such that if the first letter is "c", the second letter
        is "o" and the fourth letter is "e" then count will increase by a value of one.
        This ensures hat the 3rd character can be any string
        This loop then repeats for the length of the string inputted
        
    return the count

prompt the user to enter a string 
call the function with the users input and print a statement
 regarding the number of time the string appears.
        
"""

def wordcount(x):
    """
    

    Parameters
    ----------
    x : a string of characters
    
    Returns
    -------
    count : returns the number of time any instance of the word code appears, 
    where d can be replaced by any number or letter

    """
    count = 0
    for i in range (len(x)):
        if x[i] == 'c' and x[i+1] == 'o' and x[i+3] == 'e':
            count += 1
    return count


string = str(input('please neter a string here:'))
print("the word code appears", wordcount(string), "times")

