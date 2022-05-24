bought_food = int(input())
bought_food = bought_food * 1000
eaten_food = input()
total_eaten_food = 0
while eaten_food != 'Adopted':
    eaten_food = int(eaten_food)
    total_eaten_food += eaten_food
    eaten_food = input()
difference = abs(total_eaten_food - bought_food)
if bought_food >= total_eaten_food:
    print(f'Food is enough! Leftovers: {difference} grams.')
else:
    print(f'Food is not enough. You need {difference} grams more.')
