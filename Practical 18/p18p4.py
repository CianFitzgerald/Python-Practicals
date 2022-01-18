"""
set up the function to search the end of the strings with two areguments:
    remove case sensitivity by converting both strings to lowercase
    
    if the first word ends with the second word or vice versa:
        return true
    else:
        return false
    
prompt the user for two strings 
call the function with the users input and print the associated true or false statement
"""


def word_search(word1,word2):
    """
    

    Parameters
    ----------
    word1 : A string of characters
    word2 : A string of characters

    Returns
    -------
    bool
        Returns true if the frist word ends with the secodn or vice versa
        returns false if it does not
    """
    word1, word2 = word1.lower(), word2.lower()
    
    if word1.endswith(word2) or word2.endswith(word1):
        return True
    else:
        return False
        
string1= str(input("please enter a word here:"))
string2= str(input("please enter another word here:"))
print(word_search(string1,string2))