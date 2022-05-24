number_days = int(input())
total_food = float(input())
eaten_food_dog = 0
eaten_food_cat = 0
biscuits = 0
for days in range(1, number_days + 1):
    current_day_dog = int(input())
    current_day_cat = int(input())
    eaten_food_dog +=current_day_dog
    eaten_food_cat += current_day_cat
    if days % 3 == 0:
        biscuits += (current_day_dog + current_day_cat) * 0.1
eaten_food_total = eaten_food_dog + eaten_food_cat
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{eaten_food_total / total_food * 100:.2f}% of the food has been eaten.")
print(f"{eaten_food_dog / eaten_food_total * 100:.2f}% eaten from the dog.")
print(f"{eaten_food_cat / eaten_food_total * 100:.2f}% eaten from the cat.")
