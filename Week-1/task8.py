word= str(input())
repeat= int(input())

for char in word:
    for i in range(repeat):
        print(char, end="")

    print("")