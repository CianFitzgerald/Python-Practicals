'''
prompt the user to enter a number
initiate the cube root counter at zero
while the number entered is greater than sero or less than zero:
    while the counter cubed is less than the absolute value of the number:
        increase the counter by one
    if the counter cubedis equal to the absolute value of the number entered:
        if the counter is less than zero:
            set counter equal to -(counter)
        print the cubed root of number entere is the counter
        prompt user to enter another number
    else:
        print that the number is nota perfect cube
        break the loop
'''

number = int(input("enter the number for which you would like to check the cubed root:"))

counter = 0
while number >0 or number<0:
    while counter**3 < abs(number):
        counter += 1
        
    if counter**3 == abs(number):
        if counter<0:
            counter = -counter
        print("cubed root of", number,"is",counter)
        number = int(input("enter the number for which you would like to check the cubed root, to exit enter 0:"))
    
    else:
        print(number, "is not a perfect cube")
        break