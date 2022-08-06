number_wagons = int(input())
train = [0] * number_wagons

command = input()

while not command == "End":
    change = command.split()
    if change[0] == "add":
        train[-1] += int(change [1])
    elif change [0] == "insert":
        index = int(change[1])
        train[index] += int(change [2])
    elif change[0] == "leave":
        index = int(change[1])
        train[index] -= int(change[2])
    command = input()

print(train)
