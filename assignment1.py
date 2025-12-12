"""
#Task 1
first_name, last_name = map(str, input("Enter first and last name: ").split())
age= int(input("Age: "))
num= int(input("Phone number:"))
print("Your first name, last name:", first_name, last_name)
print("Your age:", age)
print("Your phone number:", num)
"""

"""
#Task 2
n = input("Input salaries: ")
listik= list(map(int, n.split()))
print(max(listik) - min(listik))
"""

"""
#Task 3
n= round(float(input()), 2)
print(round(((n - int(n))*100) + int(n)/100, 2))
"""

"""
#Task 4
n = int(input())
r = 1
sum = n
while True:
    if r == n:
        break
    else:
        sum += r
        r += 1
print (sum)
"""

"""
#Task 5
n1= int(input("multiply the planned number by 5: "))
n2= int(input("add 8: "))
n3= int(input("multiply the sum by 2: "))
print((16-n3)/10*(-1))
"""

"""
#Task 6
n1, op, n2= map(str, input().split())
if op == "+":
    print(int(n1) + int(n2))
if op == "-":
    print(int(n1) - int(n2))
if op == "*":
    print(int(n1) * int(n2))
if op == "/":
    print(int(n1) / int(n2))
"""

"""
#Task 7
n1, op, n2= map(str, input().split())
if op == "+":
    print(int(n1) + int(n2))
if op == "-":
    print(int(n1) - int(n2))
if op == "*":
    print(int(n1) * int(n2))
if op == "/":
    if int(n2) != 0:
        print(int(n1) / int(n2))
    else:
        print("Division by 0  is impossible")
"""
"""
#Task8
word= str(input())
repeat= int(input())

for char in word:
    for i in range(repeat):
        print(char, end="")

    print("")
"""

#Task9
num = (input())
sum1= sum(map(int, num[0:3]))
sum2= sum(map(int, num[3:]))
if sum1 == sum2:
    print("YES")
else:
    print("NO")
