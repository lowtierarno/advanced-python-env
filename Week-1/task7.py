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