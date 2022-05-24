# •	Група до 5 човека– Мусала
# •	Група от 6 до 12 – Монблан
# •	Група от 13 до 25 – Килиманджаро
# •	Група от 26 до 40 – К2
# •	Група от 41 или повече – Еверест

number_groups = int(input())
total_people = 0
people_musala = 0
people_montblan = 0
people_kolimandzharo = 0
people_k2 = 0
people_everest = 0
for group in range(number_groups):
    number_people_in_group = int(input())
    total_people += number_people_in_group
    if number_people_in_group <= 5:
        people_musala += number_people_in_group
    elif 6 <= number_people_in_group <= 12:
        people_montblan += number_people_in_group
    elif 13 <= number_people_in_group <= 25:
        people_kolimandzharo += number_people_in_group
    elif 26 <= number_people_in_group <= 40:
        people_k2 += number_people_in_group
    elif number_people_in_group >= 41:
        people_everest += number_people_in_group
print(f'{people_musala / total_people *100:.2f}%')
print(f'{people_montblan / total_people *100:.2f}%')
print(f'{people_kolimandzharo / total_people *100:.2f}%')
print(f'{people_k2 / total_people *100:.2f}%')
print(f'{people_everest / total_people *100:.2f}%')
