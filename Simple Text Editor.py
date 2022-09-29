arr = []
string = ''
ops = []

for _ in range(int(input())):
    command = input().split()
    ops.append(command)

for command in ops:
    if command[0] == '1':
        arr.append(string)
        string += command[1]
    elif command[0] == '2':
        arr.append(string)
        string = string[:-int(command[1])]
    elif command[0] == '3':
        print(string[int(command[1]) - 1])
    else:
        string = arr.pop()
