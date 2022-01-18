password_correct = "Pass123"
password = str(input("Enter your password here:")) 
if password in password_correct:
    print("you have succesfully logged in")
    
else:
    print("sorry the password is wrong")
    count = 1
    while count <= 3:
        password = str(input("Enter your password here:")) 
        if password in password_correct:
            print("You have successfully logged in") 

        else:
            print("You have been denied access.")
            break
        print()
        count += 1 
        
print("finished")




