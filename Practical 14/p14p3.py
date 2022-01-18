"""
for a number in range 2 to 20:
    for i in range 2 to the number:
        if number is exactly divible by i:
            print that the number is equal to i multiplied by its factor
            break the for loop
        else:
            print that the number is a prime number
"""

for number in range(2,20):
        for i in range(2, number):
            if number%i == 0:
                print(number,"equals",i,"*", number//i)
                break      
        else:
            print(number, "is a prime number")
            
                    
                    