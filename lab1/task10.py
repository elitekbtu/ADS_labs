sym = ''
a = []
while sym != "!":
    sym = input().strip()
    a.append(sym)

a.pop() 

method = []
for command in a:
    if command[0] == "+":
        method.insert(0, int(command[1:]))
    elif command[0] == "-":
        method.append(int(command[1:]))
    elif command[0] == "*":
        if len(method) == 0:
            print("error")
        elif len(method) == 1:
            print(method[0] * 2)
            method.pop(0)
        else:
            print(method[0] + method[-1])
            method.pop(0)
            method.pop()

