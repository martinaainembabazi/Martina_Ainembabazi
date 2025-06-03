#python considers the latest method for overloading
from multipledispatch import dispatch

@dispatch (int,int)
def product(x,y):
    return x*y
@dispatch (int,int,int)
def product (x,y,z):
    return x*y*z

print (product(2,4)) 
print (product(3,4,5))