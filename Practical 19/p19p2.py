"""
set up the base to decimal function:
    reverse the string entered 
    initialise num at 0
    for i in range zero the the length of the string
        number is assigned the ith position of the string
        if number is in the first 9 digits:
            the number is equal to the integer value of number
        else if number is in A-F:
            if number is A:
                number is equal to 10
            if number is B:
                number is equal to 11
            if number is C:
                number is equal to 12
            if number is D:
                number is equal to 13
            if number is E:
                number is equal to 14
            if number is F:
                number is equal to 15
                
        num is equal to itself plus the number multiplied by the base tot he powerof i
    return num 

prompt the user to input a number
prompt the use to enter the number of the base of the number
call the function with the users input an print the number entered to decimal
"""


def base_to_dec(string,base):
    """
    

    Parameters
    ----------
    string : the number to be converted to decimal
    base : the base of the number
    Returns
    -------
    num : The number converted to decimal form 

    """
    string = string[::-1]
    num = 0
    for i in range(len(string)):
        number = string[i]
          
        if number in "0123456789":
            number = int(number)
            
        elif number in "ABCDEF":   
            if number == "A":
                number=10
            if number == "B":
                number=11
            if number == "C":
                number=12
            if number == "D":
                number=13
            if number == "E":
                number=14
            if number == "F":
                number=15
        
        num += number*(base**i)
    return num

number = (input("enter a number here:"))
frombase = int(input("enter the base of this number:"))         
print(number, "converted to base 10 ","is:",base_to_dec(number,frombase))
