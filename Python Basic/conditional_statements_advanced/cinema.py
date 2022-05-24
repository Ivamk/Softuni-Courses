type_projection = input()
number_rows = int(input())
number_columns = int(input())

price = 0
number_places = number_columns * number_rows

if type_projection == 'Premiere':
    price = 12
elif type_projection == 'Normal':
    price = 7.50
elif type_projection == 'Discount':
    price = 5

total_income = price * number_places

print(f'{total_income:.2f} leva')

