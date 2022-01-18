amount = float(input("Enter initial amount to be taxed here:"))
print("\n")
print("Initial amount to be taxed:", amount, "\n")
large=(amount/100)*60
small=(amount/100)*40
tax1 = 0.135*large
tax2 = 0.23*small
total_tax = tax1+tax2
print("60% of initial amount taxed at 13.5% is:", tax1, "\n")
print("40% of initial amount taxed at 23% is:", tax2, "\n")
print("the amount of tax payable on inital amounnt is:", total_tax, "\n")
print("The total amount (initial amount plus taxes) is:", total_tax + amount)
