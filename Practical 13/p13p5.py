"""
set up function f with argument x:
    assign x the value x plus 1
    assign y the value 1
    assign a the value 1
    print out x, y, z and a
    return x

assign x,y,z and a the values 5,10,15,20

print out x, y, z and a

assign z to the function f with argument x
assign a to the function f with argument z

print out x, y, z and a
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
    a=1
    print("in function f:")
    print("x is", x)
    print("y is", y)
    print("z is", z)
    print("a is", a)
    return x

x,y,z,a = 5,10,15,20

print("before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)


z = f(a)

a = f(z)

print("after function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
