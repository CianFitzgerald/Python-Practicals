
'''
prompt the user to input a number for which they would like to find the square root
initiate the counter value at zero
while the number is greater than or equal to zero:
    while the counter squared is less than the absolute value of the number entered:
        increase value of counter by one
    if the counter squared is equal to the absolute value of the number entered:
        print the square root of the number is the current value of the counter
        prompt the user to enter another number
    else:
        print that the number is not a perfect sqaure
        break the loop
'''


number = int(input("enter the number for which you would like to check the square root:"))

counter = 0
while number >=0:
    while counter**2 < abs(number):
        counter += 1
        
    if counter**2 == abs(number):
        print("square root of", number,"is",counter)
        number = int(input("enter the number for which you would like to check the square root:"))
    
    else:
        print(number, "is not a perfect square")
        break