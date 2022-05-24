# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# # 	"president apartment" – 35.00 лв за нощувка

days_of_stay = int(input())
type_of_room = input()
estimation = input()
price_per_day = 0

if type_of_room == 'room for one person':
    price_per_day = 18
elif type_of_room == 'apartment':
    price_per_day = 25
elif type_of_room == 'president apartment':
    price_per_day = 35

total_price = (days_of_stay - 1) * price_per_day
if days_of_stay < 10:
    if type_of_room == 'apartment':
        total_price *= 0.7
    elif type_of_room == 'president apartment':
        total_price *= 0.9
elif 10 <= days_of_stay <=15:
    if type_of_room == 'apartment':
        total_price *= 0.65
    elif type_of_room == 'president apartment':
        total_price *= 0.85
elif days_of_stay > 15:
    if type_of_room == 'apartment':
        total_price *= 0.5
    elif type_of_room == 'president apartment':
        total_price *= 0.8

if estimation == 'positive':
    total_price *= 1.25
elif estimation == 'negative':
    total_price *= 0.9

print(f'{total_price:.2f}')
