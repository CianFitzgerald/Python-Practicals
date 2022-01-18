town = str(input("Enter town name here:"))
print("the town name you have entered is:", town)
Munster = ("Cork", "Waterford", "Limerick")
Leinster = ("Dublin", "Kilkenny")
Ulster = ("Lisburn","Belfast","Derry")
Connaught = ("Sligo" ,"Galway")


if town in Munster:
    print("You entered", town + '.',town,"is in Munster.")
    
elif town in Leinster:
    print("You entered",town + '.',town, "is in Leinster.")
    
elif town in Ulster:
    print("You entered",town + '.',town, "is in Ulster.")
    
elif town in Connaught:
    print("You entered",town + '.',town, "is in Connaught.")
    
else:
    print("Sorry, I didn't recognise that name.")



