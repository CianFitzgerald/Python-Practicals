'''
prompt the useer to enter a number 
initiate the total value of the summation at 0
initiate the count at 0
while the count is less than or equal to the number entered 
and the number is greater than or equal to one:
    total is equal to the total plus the count 
    the count is increased by a value of one 
print out the total summation of the integers
'''

number = int(input("please eneter a positive integer here:"))
print("number entered is:", number)
total = 0
count = 0
while count<=number and number>=1:
    total += count
    count += 1
print("the summation of the first", number, "integers is", total)