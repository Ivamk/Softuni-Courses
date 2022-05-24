from math import floor, ceil

number_days = int(input())
food_left = int(input())
food_dog_per_day = float(input())
food_cat_per_day = float(input())
food_turtle_per_day = float(input())

total_food_kg = number_days * (food_dog_per_day + food_cat_per_day + food_turtle_per_day/1000)

difference = abs(total_food_kg - food_left)

if food_left >= total_food_kg:
    print(f'{floor(difference)} kilos of food left.')
else:
    print(f'{ceil(difference)} more kilos of food are needed.')

