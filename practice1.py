"""
#Task1

n= int(input())
print(round((9/5)*n +32, 1))
"""

"""
#Task2

op = input("Choose operation (+, -, *, /) ")
n1, n2= map(str, input("Enter two numbers: ").split())
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
#Task3

n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

"""
#Task4

def is_alive(health): 
    if health < 0:
        return False 
    else:
        return True
"""


#Task5

month= int(input("Enter number of the month of your birth: "))

def season_events(number_of_month):
    if number_of_month == 12 or number_of_month == 1 or number_of_month == 2:
        print("White snow fell outside the window")
    elif 3 <= number_of_month <= 5:
        print("Birds sang beautiful songs")
    elif 6 <= number_of_month <= 8:
        print("The sun shone brighter than ever")
    elif 9 <= number_of_month <= 11:
        print("The harvest was incredible")
    else:
        print ("You need to enter the real number of the month")

season_events(month)