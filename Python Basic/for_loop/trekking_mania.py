number_groups = int(input())
group_musala = 0
group_montblan = 0
group_kalimandzharo = 0
group_k2 = 0
group_everest = 0
for sequence in range(number_groups):
    number_people_in_group = int(input())
    if number_people_in_group <= 5:
        group_musala += number_people_in_group
    elif 6 <= number_people_in_group <= 12:
        group_montblan += number_people_in_group
    elif 13 <= number_people_in_group <= 25:
        group_kalimandzharo += number_people_in_group
    elif 26 <= number_people_in_group <= 40:
        group_k2 += number_people_in_group
    elif number_people_in_group >= 41:
        group_everest += number_people_in_group
total_people = group_montblan + group_k2 + group_musala + group_everest + group_kalimandzharo
p1 = group_musala / total_people * 100
p2 = group_montblan / total_people * 100
p3 = group_kalimandzharo / total_people * 100
p4 = group_k2 / total_people * 100
p5 = group_everest / total_people * 100
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')

