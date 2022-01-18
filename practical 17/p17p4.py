"""
set up function to check if a string is a palindrome:
    set up function to convert string to lowercase and remove non letters:
        use s.lower to convert all character to lower case
        initialise empty string variable
        for c in s:
            if c is in the alphabet:
                add c to the empty string 
        return the string 
    
    set up function to check if string is a palindrome:
        if the length of s is less than or equal to one:
            return True
        else:
            compare the first and last letters and check the remainder of the string
            
        return this function witht the second fuction as it's input
    
prompt the user to enter a string
while this is not an empty string:
    if the the string entered is a palindrome (using original function):
        print that it is a palindrome
    else:
        print that the string is not a palindrome 
    prompt the user to enter another string
        
    
"""



def isPalindrome(s):
    """
    

    Parameters
    ----------
    s : a string of characters

    Returns
    -------
    Whether the string is a palindrome or not

    """
    def toChar(s):
        """
        

        Parameters
        ----------
        s : a string of characters

        Returns
        -------
        letterstring : a string of characters, all of which are lowercase and no non-letters

        """
        s= s.lower()
        letterstring =""
        for c in s:
            if c in "abcdefghijklmnopqrstyvwxyz":
                letterstring +=c
        return letterstring


    def isPal(s):
        """
        

        Parameters
        ----------
        s : a string of characters

        Returns
        -------
        isPal(toChar(s)): a recursive function checking if letterstring is a palindrome

        """
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))
     

string = input("enter an string (empty string to exit):")
while str != "":
    if isPalindrome(string):
       print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")
    string = input("enter an string (empty string to exit")
        
    