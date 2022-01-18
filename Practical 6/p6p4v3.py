password_correct = "Password123"
count = 1
while count <= 3:
    password = str(input("Enter your password here:")) 
    if password in password_correct:
        print("you have successfully logged in")
        
        
    else:
        print("You have been denied access.")
        
    count += 1 


