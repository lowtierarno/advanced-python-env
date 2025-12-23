n= input()
if n[0] == "x" and n[1] == "+":
    print(int(n[4]) - int(n[2]))
if n[0] == "x" and n[1] == "-":
    print(int(n[4]) + int(n[2]))
if n[2] == "x" and n[1] == "+":
    print(int(n[4]) - int(n[0]))
if n[2] == "x" and n[1] == "-":
    print(int(n[0]) - int(n[4]))