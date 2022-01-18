'''
prompt user to enter a number
while the number entered is greater than zero:
    if number is exactly divisible by two 
        print that the number is divisible by two
    if number is exactly divisible by three
        print that the number is divisible by three
    if number is exactly divisible by five  
        print that the number is divisible by five
    if number is exactly divisible by seven
        print that the number is divisible by seven
        
    prompt user ot input another number, 
    notifying them that if the number is
    negative that the program wil terminate
'''

number = int(input("enter a number here:"))
print("The number you have entered is:", number)
while number >= 0:
    if number % 2 == 0:
        print("number is divisible by 2")
    if number % 3 == 0:
        print("number is divisible by 3")
    if number % 5 == 0:
        print("number is divisible by 5")
    if number % 7 == 0:
        print("number is divisible by 7")
        
        
    number = int(input("enter a number here. To terminate program, enter a negative number:"))
    