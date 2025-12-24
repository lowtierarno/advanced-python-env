import math


def heron(side1, side2, side3):
    p = (side1 + side2 + side3) / 2
    return math.sqrt(p * (p - side1) * (p - side2) * (p - side3))


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
k = float(input("k: "))


area1 = heron(a, b, k)
area2 = heron(c, d, k)

total = area1 + area2
print(total)