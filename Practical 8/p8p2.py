'''
prompt user to enter a number
initiate i at 1 
while i is less than or equal to the number entered:
    initiate j at 1 
    while j is less than or equal to the number entered:
        print i multiplied by j
        increase the value of j by one 
    print new line
    increase the value of i by one
'''
number = int(input("Enter the size of the table:" ))
print("The number you have entered is:", number)
i = 1
while i <= number:
    j=1
    while j <= number:
        print(i*j, "", end = "")
        j += 1
    print()
    i += 1
    

