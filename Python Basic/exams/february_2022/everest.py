start = 5364
finish = 8848
command = input()
count_days = 1
is_reached = False
while command != 'END':
    if command == 'Yes':
        count_days += 1
    climb_mettres = int(input())
    if count_days > 5:
        break
    start += climb_mettres
    if start >= finish:
        is_reached = True
        break
    command = input()
if is_reached:
    print(f'Goal reached for {count_days} days!')
else:
    print(f'Failed!')
    print(f"{start}")
