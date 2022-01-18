"""
set up function f with argument x:
    assign x the value x plus 1
    assign y the value 1
    print out x, y and z
    return x

assign x,y and z the values 5,10,15

print out x,y and z

assign z to the function f with argument x

print out x,y and z 
"""

def f(x):
    """
    

    Parameters
    ----------
    x : integer.

    Returns
    -------
    x : returns the print functions with input x

    """
    x+=1
    y=1
    print("in function f:")
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return x

x,y,z = 5,10,15

print("before function f:")
print("x is", x)
print("y is", y)
print("z is", z)

z = f(x)

print("after function f:")
print("x is", x)
print("y is", y)
print("z is", z)