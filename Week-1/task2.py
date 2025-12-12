n = input("Input salaries: ")
listik= list(map(int, n.split()))
print(max(listik) - min(listik))