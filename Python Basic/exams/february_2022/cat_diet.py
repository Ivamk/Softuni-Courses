oil = int(input())
protein = int(input())
vaglehidrates = int(input())
total_calories = int(input())
percentage_water = int(input())

total_oils = (total_calories * oil / 100) / 9
total_protein = (total_calories * protein / 100) / 4
total_vaglehidrates = (total_calories * vaglehidrates / 100) / 4
weight = total_vaglehidrates + total_oils + total_protein
calories_per_gram = total_calories / weight
calories_per_gram = calories_per_gram - calories_per_gram * percentage_water / 100
print(f'{calories_per_gram:.4f}')

