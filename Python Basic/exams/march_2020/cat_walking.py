walking_minutes_per_day = int(input())
number_walking_day = int(input())
kcal_per_day = int(input())
decrease_kcal = walking_minutes_per_day * number_walking_day * 5
percent_kcal = kcal_per_day / 2
if decrease_kcal >= percent_kcal:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {decrease_kcal}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {decrease_kcal}.')
