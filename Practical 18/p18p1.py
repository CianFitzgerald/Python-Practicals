"""
set up the ispal function with argument s:
    ensure that all characters are lowercase using .lower
    initialise word as an empty string 
    for c in s:
         if c is in the alphabet 
             add that letter to the word
             
        pal is assigned true
        for i in range 0 to half the length of the string entered by the user:
            if the first letter is not equal to the last letter:
                pal is assigned false
                this loop repeats for each letter 
                loop breaks if false
                
        return pal

prompt user to enter a string 
while the string is not an empty string:
    if ispal function is true for the gievn input:
        print that the word is a palindrome 
    else:
        print that the word is not a palindrome 
    prompt user for another string 

"""


def isPal(s):
    """
    

    Parameters
    ----------
    s : string of characters entered by the user

    Returns
    -------
    pal : Returns true if the string entered is a palindrome,
    Returns false otherwise.
    """
    s = s.lower()
    word =""
    for c in s:
        if c in "abcdefghijklmnopqrstyvwxyz":
            word +=c

    pal = True
    for i in range(0,len(word)//2):
        if word[i] != word[len(word)-i-1]:
            pal = False
            break
    
    return pal


string = input("enter an string (empty string to exit):")
while str != "":
    if isPal(string):
       print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")
    string = input("enter an string (empty string to exit):")
     
    
