'''
prompt the user for the number of possible toppings (n)
prompt the user for the number of toppings offered on a standard pizza (k)

initiate the factorial of n at 1
initiate the factorial of k at 1
initiate the factorial of n-k at 1

set up for loop in range n to n+1:
    set factorial of n equal to itself multiplied by the range x

set up for loop in range n to n+1:
    set factorial of k equal to itself multiplied by the range y

set up for loop in range n to n+1:
    set factorial of (n-k) equal to itself multiplied by the range z
    
set up the formula for the number of combinations
fill into the equation with the variables created using the for loops

print the number of combinations possible 
'''


n = int(input("please enter the number of possible toppings:"))
k = int(input("how many toppings are offered on the standard pizza:"))

n_fact = 1
k_fact = 1
nk_fact = 1


for x in range (1, n+1 , 1):
    n_fact *= x
 

for y in range (1, k+1 , 1):
    k_fact *= y


for z in range (1, (n-k)+1 , 1):
    nk_fact *= z


combinations = (n_fact)/(k_fact*nk_fact)
print("the number of combinations of", k, "standard pizzas from", n, "possible toppings is", combinations)