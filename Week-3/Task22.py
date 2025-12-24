def rectangle(a, b):
    return a*b

for i in range(3):
    a= int(input("Length: "))
    b= int(input("Width: "))

    print(f"Area: {rectangle(a,b)}")