capacity_stadium = int(input())
number_of_all_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0
for sequence in range(number_of_all_fans):
    sector_for_each_fan = input()
    if sector_for_each_fan == 'A':
        fans_a += 1
    elif sector_for_each_fan == 'B':
        fans_b += 1
    elif sector_for_each_fan == 'V':
        fans_v += 1
    elif sector_for_each_fan == 'G':
        fans_g += 1
percentage_fans_a = fans_a / number_of_all_fans * 100
percentage_fans_b = fans_b / number_of_all_fans * 100
percentage_fans_v = fans_v / number_of_all_fans * 100
percentage_fans_g = fans_g / number_of_all_fans * 100
percentage_all_fans = number_of_all_fans / capacity_stadium * 100
print(f'{percentage_fans_a:.2f}%')
print(f'{percentage_fans_b:.2f}%')
print(f'{percentage_fans_v:.2f}%')
print(f'{percentage_fans_g:.2f}%')
print(f'{percentage_all_fans:.2f}%')
