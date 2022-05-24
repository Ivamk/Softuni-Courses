lenght_m = float(input())
width_m = float(input())

width_cm_without_corridor = width_m * 100 - 100
lenght_cm = lenght_m * 100

number_desks_per_row = width_cm_without_corridor // 70
number_rows = lenght_cm // 120

number_working_places = number_desks_per_row * number_rows - 3

print(f'{number_working_places:.0f}')

