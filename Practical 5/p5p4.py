number = int(input("Enter a number here:"))
print("The number you have entered is:", number)
if number == 0:
    print("this number is equal to 0")
elif number>0 and number<=20:
    print("Number is greater than 0 and less than or equal to 20")
elif number>20 and number<=40:
    print("Number is greater than 20 and less than or equal to 40")
elif number>40 and number<=60:
    print("Number is greater than 40 and less than or equal to 60")
elif number>60 and number<=80:
    print("Number is greater than 60 and less than or equal to 80")
elif number>80 and number<=100:
    print("Number is greater than 80 and less than or equal to 100"
          )
elif number>100:
    print("Number is greater than 100")
else:
    print("The number you have entered is negative, please try again.")