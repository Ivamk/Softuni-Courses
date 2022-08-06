neighbour = [int(el) for el in input().split("@")]
current_position = 0
commands = input().split()

while not commands[0] == "Love!":
    move = int(commands[1])
    current_position += move
    if current_position >= len(neighbour):
        current_position = 0
    if neighbour[current_position] <= 0:
        print(f"Place {current_position} already had Valentine's day.")
    else:
        neighbour[current_position] -= 2
        if neighbour[current_position] <= 0:
            print(f"Place {current_position} has Valentine's day.")

    commands = input().split()
print(f"Cupid's last position was {current_position}.")
count_zeros = neighbour.count(0)
if count_zeros == len(neighbour):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighbour) - count_zeros} places.")
