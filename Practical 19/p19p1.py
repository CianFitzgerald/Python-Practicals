"""
set up the conversion function with two arguments the number and the base 
    assign the variable num to the the first nine digits and A-F of the alphabet
    if the number entered is less than the base:
        return the associated number of the string of digits for the number entered
    else:
        return the conversion function where the first argument is the number divided by the base 
        and the second is the base itself plus the associated number of the string of digits for the modulus 
        of the operands number and base.
        
** how this recursion works - a number is input with a given base, if the number is greater than the base
then the input will go into the recursive part of the function, this recursion will continue until 
the base is less than the number, in which case it will return the associated digit or letter from the string num.
The recursion will then progress towards the base case, within each step the modulus of number divided by base is calculated 
and the associated digit or letter of the string num is returned and added to the returned value until the recursion is finished.**

prompt the user to enter a number in base 10
prompt the user to enter the base to which they would like to convet
call the function with these numbers inputted and print the relevant statements



"""


def conversion(number,base):
    
    """
    
    Parameters
    ----------
    number : number in base 10 
    base : base to which the number will be converted
    
    Returns
    -------
    returns the number in whichever base is chosen by the user

    """
    
    
    num = "0123456789ABCDEF"
    if number < base:
       return num[number]
    else:
       return conversion(number//base,base) + num[number % base]


number = int(input("enter a number here in base 10:"))
tobase = int(input("enter the base to which you would like to convert:"))         
print(number, "converted to base", tobase,"is:",conversion(number,tobase))
