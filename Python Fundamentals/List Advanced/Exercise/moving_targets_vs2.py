def is_valid(index, lst):
    if 0 <= index < len(lst):
        return True
    return False


def shoot(lst, index, power):
    if is_valid(index, lst):
        lst[index] -= power
        if lst[index] <= 0:
            lst.pop(index)
    return lst


def add(lst, index, power):
    if is_valid(index, lst):
        lst.insert(index, power)
        return lst
    print("Invalid placement!")


def strike(lst, index, power):
    if is_valid(index, lst) and is_valid(index-power, lst) and is_valid(index+power, lst):
        del lst[index-power:index+power+1]
        return lst
    print("Strike missed!")


targets = [int(el) for el in input().split()]
command = input()
while not command == "End":
    command = command.split()
    index = int(command[1])
    number = int(command[2])
    if command[0] == "Shoot":
        shoot(targets, index, number)
    elif command[0] == "Add":
        add(targets, index, number)
    elif command[0] == "Strike":
        strike(targets, index, number)
    command = input()
print(*targets, sep="|")
