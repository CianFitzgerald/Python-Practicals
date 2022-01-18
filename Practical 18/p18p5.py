"""
set up the function that searches for "xyz" and ".xyz", with argument x:
    for i in range zero to the length of x minus 2:
        if the string contains 3 consecutive letters which are "xyz" and 
        if the preceding charcter of this string is not a "."
            return true
        else:
            return false
        
prompt the user to enter a string 
call the function with the users input and print the associated true or false statement 
"""



def xyz_search(x):
    """
    

    Parameters
    ----------
    x : A string of characters

    Returns
    -------
    bool
    returns true if xyz appears where a . does not preceed it 
    returns false otherwise
        

    """
    for i in range(len(x)-2):
        if x[i:i+3] == "xyz" and x[i-1:i] != ".":
            return True
        else:
            return False

string = (input("enter a string here:"))
print(xyz_search(string))