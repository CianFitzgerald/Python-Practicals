'''
PSEUDOCODE:
    
set up the running total, starting at zero
set up the counter and initiate at one 
while the counter is less than 10000:
    if the counter is exactly divisible by three or exactly divisible by five
        add the total to the value of the count 
    add one to the counter 
print the running total 

'''

total  = 0
count = 1
while (count <= 10000):
    if ((count % 3 == 0) or (count % 5==0)):
        total += count
    count += 1 
     
print(total)