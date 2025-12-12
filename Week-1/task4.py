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