capacity_luggage = float(input())
volume_luggage = input()
number_luggage = 0
free_space = True
while volume_luggage != 'End':
    volume_luggage = float(volume_luggage)
    number_luggage += 1
    if number_luggage % 3 == 0:
        volume_luggage *= 1.1
    if capacity_luggage >= volume_luggage:
        capacity_luggage -= volume_luggage
    else:
        free_space = False
        number_luggage -= 1
        break
    volume_luggage = input()
if not free_space:
    print(f"No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")
print(f'Statistic: {number_luggage} suitcases loaded.')