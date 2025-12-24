def gcd(a,b ):
    while b:
        a, b = b, a%b
    return a

a = int(input(""))
b = int(input(""))

# Расчет
gcd = gcd(a, b)
lcm = (a * b) // gcd

print(f"GCD: {gcd}")
print(f"LCM: {lcm}")