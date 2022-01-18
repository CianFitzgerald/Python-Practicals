"""
define the word count function with argument x:
    assign the string "code" to the variable word
    assign the count of th variable word to the variable count
    if count is greater than 1:
        return count
    else:
        return zero
prompt the user to enter a string 
call the function with the users input and print a statemnt regarding the 
number of times code appears in the string
"""



def wordcount(x):  
    """
    

    Parameters
    ----------
    x : A string of characters

    Returns
    -------
    returns the amount of times the string code appears

    """
    word = "code"
    count = x.count(word)
    if count>=1:
        return count
    else:
        return 0

string = str(input('please neter a string here:'))
print("the word code appears", wordcount(string), "times")

