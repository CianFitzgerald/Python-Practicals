'''
PSEUDOCODE:
    
Set the password to be stored in the programme (Pass123)
Prompt the user to enter password
if password is correct
    print you have successfully logged in & terminate program
    
else: prompt user for another password

if second password is correct
     print you have successfully logged in & terminate program
    
else: prompt user for a third Password

if third password is correct
    print you have successfully logged in & terminate program
    
else: notify user that access has been denied
    
'''


import sys
password_correct = "Pass123"
password1 = str(input("Enter your password here:")) 

if password1 in password_correct:
    print("you have successfully logged in")
    sys.exit()
    
else:     
    password2 = str(input("Enter your password here:")) 
        
    if password2 in password_correct:
        print("you have successfully logged in")
        sys.exit()
    
    else:     
        password3 = str(input("Enter your password here:")) 
               
        if password3 in password_correct:
            print("you have successfully logged in")
            sys.exit()
            
        else: 
            print("You have been denied access")
                

    
  


    


