'''
PSEUDOCODE:
    
set up a running total and initiate at zero
set up a counter and initiate at the first integer, which is zero
while the counter is less than 4999
    add the counter to the total
    add one to the counter each time 
print the total summation

'''



total = 0
count=0
while count <= 4999:
    total = total + count
    count += 1
    
print("Total summation of first 5000 integers is:", total)