def gcd(a,b ):
    while b:
        a, b = b, a%b
    return a

a= int(input())
b= int(input())
c= int(input())
d= int(input())

common= gcd(b, d)

num= a*common - c*common
den= b*d

print(f"Result: {num//common}/{den // common}")