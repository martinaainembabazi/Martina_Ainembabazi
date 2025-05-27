from multipledispatch import dispatch
@dispatch (int,int,int)
def sum(x,y,z):
     result=x+y+z
     print(result)

@dispatch (float,float,float)
def sum(w,r,t):
 result=w+r+t
 print(result)

sum(2,3,4)
sum(6.1,7.9,9.0)
