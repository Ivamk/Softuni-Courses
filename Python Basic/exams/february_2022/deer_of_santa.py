from math import ceil, floor
number_days = int(input())
left_food = int(input())
first_deer = float(input())
second_deer = float(input())
third_deer = float(input())
needed_food = number_days * (first_deer + second_deer + third_deer)
difference = abs(left_food - needed_food)
if left_food >= needed_food:
    print(f'{floor(difference)} kilos of food left.')
else:
    print(f'{ceil(difference)} more kilos of food are needed.')
