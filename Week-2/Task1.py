n= input()
sum= 0
for i in range(len(n)-4):
    a = n[i:i+5]
    if a == ">>-->" or a == "<--<<":
        sum += 1
print(sum)