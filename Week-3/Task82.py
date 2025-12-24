m= int(input("Length: "))
a= []

for i in range(m):
    r= int(input("Enter number: "))
    a.append(r)

print(a)

a[0], a[-1] = a[-1], a[0]

print(a)