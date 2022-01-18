'''
prompt the user to enter a number
initiate the counter for the seven different ranges at zero
while the number entered is greater than or equal to zero:
    if the number is equal to zero:
        print that the number is euqal to zero
        add one to the first range 
    elseif the number is is greater than 0 and less than or equal to 20:
        print that the number is is greater than 0 and less than or equal to 20
        add one to the second range 
    elseif the number is is greater than 20 and less than or equal to 40:
        print that the number is is greater than 0 and less than or equal to 20
        add one to the third range 
    elseif the number is greater than 40 and less than or equal to 60:
        print that the number is greater than 40 and less than or equal to 60
        add one to the fourth range 
    elseif the number is greater than 60 and less than or equal to 80:
        print that the number is greater than 60 and less than or equal to 80
        add one to the fifth range 
    elseif the number is greater than 80 and less than or equal to 100:
        print that the number is greater than 80 and less than or equal to 100
        add one to the sixth range 
    elseif the number is greater than 100:
        print that the number is euqal to zero
        add one to the seventh range 
        
    prompt user ot input another number, 
    notifying them that if the number is
    negative that the program wil terminate
        
print out statements regarding input analysis i.e print out the total of each range
    

'''


number = int(input("Enter a number here:"))
print("The number you have entered is:", number)
range1, range2, range3, range4, range5, range6, range7 = 0,0,0,0,0,0,0

while number>=0:
    if number == 0:
        print("this number is equal to 0")
        range1 += 1
    elif number>0 and number<=20:
        print("Number is greater than 0 and less than or equal to 20")
        range2 += 1
    elif number>20 and number<=40:
        print("Number is greater than 20 and less than or equal to 40")
        range3 += 1
    elif number>40 and number<=60:
        print("Number is greater than 40 and less than or equal to 60")
        range4 += 1
    elif number>60 and number<=80:
        print("Number is greater than 60 and less than or equal to 80")
        range5 += 1            
    elif number>80 and number<=100:
        print("Number is greater than 80 and less than or equal to 100")
        range6 += 1
    elif number>100:
        print("Number is greater than 100")
        range7 += 1
    
    number = int(input("Enter a number here, enter negative number to terminate:"))
    
print("\n")
print("analysis of input")
print("number of numbers equal to 0:", range1)
print("number of numbers greater than 0 and less than or equal to 20:", range2)
print("number of numbers greater than 20 and less than or equal to 40:", range3)
print("number of numbers greater than 40 and less than or equal to 60:", range4)
print("number of numbers greater than 60 and less than or equal to 80:", range5)
print("number of numbers greater than 80 and less than or equal to 100:", range6)
print("number of numbers greater than 100:", range7)
