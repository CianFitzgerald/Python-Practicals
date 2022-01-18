town = str(input("Enter town name here:"))


if town == "Cork" or town =="Waterford" or town == "Limerick":
    print("You entered",town,',',town,"is in Munster.")
    
elif town == "Dublin" or town =="Kilkenny":
    print("You entered",town,',',town, "is in Leinster.")
    
elif town == "Lisburn" or town == "Belfast" or town == "Derry":
    print("You entered",town,',',town, "is in Ulster.")
    
elif town == "Sligo" or town == "Galway":
    print("You entered",town,',',town, "is in Connaught.")
    
else:
    print("Sorry, I didn't recognise that name.")


    
