"""
#Task1
n= input()
words= n.lower().split()
sum= 0
for s in words:
    if s[0] == 'е':
        sum += 1
print(sum)"""
"""
#Task2
n= input()
count = n.count(":")
newn = n.replace(':', '%')
print("Num of replacements:", count)
print(newn)"""

"""
#Task3
n= input()
count = n.count(".")
newn = n.replace('.', '')
print("Num of removed char:", count)
print(newn)
"""
"""
#Task4
n= input()
chars= n.count('')
count = n.count("а")
newn = n.replace('а', 'о')
print("Num of replacements", count)
print("Num of characters", chars)
print(newn)
"""
"""
#Task5
n= input()
new= n.lower()
print(new)
"""

"""
#Task6
n= input()
count = n.count("а")
newn = n.replace('а', '')
print("Num of removed char:", count)
print(newn)
"""
"""
#Task7
n= input()
count = n.count("")
half= int(count/2)
first= n[:half]
sec= n[half:]
newn = first.replace('n', '*')
print(newn+sec)
"""
"""
#Task8
n= input()
count = len(n.split())
print("Num of words:", count)
"""
"""
#Task9
n= input()
find= input("Word to find: ")
words= n.split()
count= words.count(str(find))
print(count)
"""
"""
#Task10
n= input()
newn = n.title()
print(newn)
"""
"""
#Task11
n= input()
count = n.count("а")
newn = n.replace('!', '.')
seq= 0
max_seq= 0
for char in n:
    if char == "n":
        seq += 1
        if seq > max_seq:
            max_seq = seq
    else:
        seq = 0
print("Num of longest sequence:", max_seq)
print(newn)
"""
"""
#Task12
n= input()
words= n.split()
k = []
for i in words:
    if i[-1] == "l":
        k.append(i)
print(k) 
"""
"""
#Task13
n = input()
start= n.find("[")
end= n.find("]")
newn = n[start+1 : end]
print(newn)
"""
"""
#Task14
n= input()
words= n.split()
k = []
r= []
for i in words:
    if i[-1] == "l":
        k.append(i)
    if i[0] == "a":
        r.append(i)
print("End with l: ", k)
print("Start with a:",r)
"""

#Task15
n= input()
count= n.count("t")
print(count)