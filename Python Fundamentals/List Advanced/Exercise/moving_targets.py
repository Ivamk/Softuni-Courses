targets = [int(el) for el in input().split()]
command = input().split()
while not command[0] == "End":
    index = int(command[1])
    value = int(command[2])
    if command[0] == "Shoot":
        if index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif command[0] == "Add":
        if index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")
    elif command[0] == "Strike":
        if 0 <= index - value < len(targets) and 0 <= index + value < len(targets):
            targets = targets[0:index-value] + targets[index + value + 1::]
        else:
            print(f"Strike missed!")
    command = input().split()

print(*targets, sep="|")
