if __name__ == '__main__':
    N = int(input())
    list= []
    def inserting(a,b):
        list.insert(a,b)
    def remove(e):
        list.remove(e)
    def append(e):
        list.append(e)
    for i in range(N):
        commands = input().split()
        command = commands[0]
        if command == "insert":
            inserting(int(commands[1]), int(commands[2]))
        elif command == "print":
            print(list)
        elif command == "remove":
            remove(int(commands[1]))
        elif command == "append":
            append(i)
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()