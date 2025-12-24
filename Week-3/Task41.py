def gcd(a,b ):
    while b:
        a, b = b, a%b
    return a

a= int(input())
b= int(input())
c= int(input())
d= int(input())

num= a * d
denom= b * c

common= gcd(num, denom)
fin= num // common
findenom = denom // common

print(f"Result: {fin}/{findenom}")