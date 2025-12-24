def square():
    n= int(input())
    return(n**2)
def circle():
    p= 3.14
    r= int(input())
    return(p*(r**2))
def rectangle():
    a= int(input())
    b= int(input())
    return(a*b)

n= input("Choose shape: Square, circle or rectangle: ").lower()
if n == "square":
    square()
if n == "rectangle":
    rectangle()
else:
    circle()