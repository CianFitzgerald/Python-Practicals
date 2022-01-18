amount = 202067.73
large_amount=(amount/100)*60
small_amount=(amount/100)*40
tax1 = 0.135*large_amount
tax2 = 0.23*small_amount
total_tax = tax1+tax2
print(total_tax + amount)