a= input()
b= input()

n= len(a)
m= len(b)
bb= b+b
shifts= set()
for i in range (m):
    shifts.add(bb[i:i+m])

sum = 0
for i in range(n - m + 1):
    suba = a[i:i+m]
    if suba in shifts:
        sum += 1
print(sum)
