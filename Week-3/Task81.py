n= int(input())
res= []
for i in range(1, n+1):
    nums = [int(d) for d in str(i)]
    if 0 in nums:
        continue
    if all(i % d == 0 for d in nums):
        res.append(i)

print(res)