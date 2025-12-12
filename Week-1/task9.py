num = (input())
sum1= sum(map(int, num[0:3]))
sum2= sum(map(int, num[3:]))
if sum1 == sum2:
    print("YES")
else:
    print("NO")