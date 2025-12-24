def is_inside(x, y, a, b, R):
    return (x - a)**2 + (y-b)**2 <= R**2

a= int(input("Circle center a: "))
b= int(input("Circle center b: "))
R= int(input("Radius: "))

points= {
    "p": (int(input("P x: ")), int(input("P y: "))),
    "f": (int(input("f x: ")), int(input("f y: "))),
    "l": (int(input("l x: ")), int(input("l y: ")))
}

sum = 0
for name, (x,y) in points.items():
    if is_inside(x,y,a,b,R):
        sum+=1 
        print(f"{name} is inside")
    else:
        print(f"{name} is outside")

print(f"Number of points inside: {sum}")