def square():
    n= int(input())
    print(n**2)
def circle():
    p= 3.14
    r= int(input())
    print(p*(r**2))
def rectangle():
    a= int(input())
    b= int(input())
    print(a*b)

n= input("Choose shape: Square, circle or rectangle: ").lower()
if n == "square":
    square()
if n == "rectangle":
    rectangle()
else:
    circle()