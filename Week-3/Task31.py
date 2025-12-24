import math
h= []
for i in range(2):
    print(f"Triangle {(i+1)}")
    a= int(input())
    b= int(input())
    hypo= math.sqrt(a**2 + b**2)
    print(f"Hypothenus {i+1}: {hypo:.2f}")
    h.append(hypo)
print(f"Greater hypothenus: {(max(h)):.2f}")