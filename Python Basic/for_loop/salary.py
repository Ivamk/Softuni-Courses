number_tabs_opened = int(input())
salary = float(input())
sum_fine = 0
for sequence in range(number_tabs_opened):
    name_browser = input()
    if name_browser == 'Facebook':
        sum_fine += 150
    elif name_browser == "Instagram":
        sum_fine += 100
    elif name_browser == 'Reddit':
        sum_fine += 50
    else:
        sum_fine += 0
    if sum_fine >= salary:
        break
difference = abs(sum_fine - salary)
if sum_fine >= salary:
    print('You have lost your salary.')
else:
    difference = difference // 1
    print(f'{difference:.0f}')
