'''
PSEUDOCODE:
    
Set the password to be stored in the programme (Pass123)
Prompt user for a password
If the password is correct
    Notify user acces has been granted and terminate programme 
    
else password is incorrect
    notify user that it is incorrect 
    
notify user that the password was incorrect and that they must enter the 
password correctly three times to gain access 

prompt user to enter the password three times

if any of the three entries is incorrect then notify user that access has been 
denied and terminate programme

else if all three entries are correct notify the user that access has been granted 
and terminate programme



'''


import sys
password_correct = "Pass123"
password = str(input("Enter your password here:")) 

if password in password_correct:
    print("you have succesfully logged in")
    sys.exit()

else:
    print("Sorry, the password is wrong.", "\n")
    
    print("Enter password correctly three times to gain access.")      
    password1 = str(input("Enter your password here:")) 
    password2 = str(input("Enter your password here:")) 
    password3 = str(input("Enter your password here:")) 
    
    if password1 and password2 and password3 not in password_correct:
        print("access denied")
        
    else: 
        print("access granted")
        

    