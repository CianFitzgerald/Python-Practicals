'''
prompt the user to enter a number 
initiate y at 0 ( where y is the first number of the times table column)
while y is less than or equal to twenty:
    print the value of y and the value of y multiplied by the number entered
    increase the value of y by one
'''


number = int(input("please neter a number here:"))
print("The number you have entered is:", number)
y = 0
print("times",number,"tables")
while y <= 20:
    print(y, number*y)
    y += 1


