weight = int(input())
lenght = int(input())
height = int(input())
allowed_space = weight * lenght * height
sum_boxes = 0
is_moved = True
while sum_boxes <= allowed_space:
    command = input()
    if command == 'Done':
        is_moved = False
        break
    else:
        command = int(command)
        sum_boxes += command
difference = abs(sum_boxes - allowed_space)
if is_moved:
    print(f'No more free space! You need {difference} Cubic meters more.')
else:
    print(f'{allowed_space - sum_boxes} Cubic meters left.')
