'''
PSEUDOCODE:
    
Prompt user to input name 
if the name they input is cian 
    print that's a cool name 
if the the name they input is spongebob squarepants or mickey mouse
    print that's not your name 
otherwise print that they have a nice name 

'''


your_name = str(input("please enter your name here:"))
if your_name == ("Cian"):
    print("That is a cool name!")
elif your_name in ("Spongebob Squarepants", "Mickey Mouse"):
    print("I'm not sure if that is your name, please try again!")
else:
    print("You have a nice name.")