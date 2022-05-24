num_floors = int(input())
num_rooms = int(input())
for floors in range(num_floors, 0, -1):
    for rooms in range(num_rooms):
        if floors == num_floors:
            print(f'L{num_floors}{rooms}', end=' ')
        elif floors % 2 == 1:
            print(f'A{floors}{rooms}', end=' ')
        elif floors % 2 == 0:
            print(f'O{floors}{rooms}', end=' ')
    print()

