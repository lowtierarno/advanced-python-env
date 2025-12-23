n= input().split()

freq= {}

for i in n:
    freq[i] = freq.get(i, 0) + 1

print("Purchase frequency:")
for i, count in freq.items():
    print(f"{i}: {count}")

pop= max(freq, key=freq.get)
print(f"Most popular item: {pop}")

one = [i for i, count in freq.items() if count == 1]
print(f"Purchased once: {one}")

sort = sorted(freq.items(), key=lambda x: x[1], reverse= True)
print("Sorted by frequency")
for i, count in sort:
    print(f"{i} {count}")