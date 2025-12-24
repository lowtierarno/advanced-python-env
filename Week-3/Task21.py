import math

def triangle(s):
    return (math.sqrt(3) / 4) * (s ** 2)

a= int(input())
hexag = 6 * triangle(a)

print(f"The area of hexagon is: {hexag:.2f}")