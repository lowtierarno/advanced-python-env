import math

def triangle(a, b):
    return (a*b) / 2

def heron(side1, side2, side3):
    p = (side1 + side2 + side3) / 2
    return math.sqrt(p * (p - side1) * (p - side2) * (p - side3))

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
t = int(input("t: "))

s1= triangle(x,y)

d= math.sqrt(x**2 + y**2)

s2= heron(z, t, d)

print(f"Area: {s1+s2}")