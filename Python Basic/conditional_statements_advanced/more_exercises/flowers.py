# if season == 'Autumn' or season == 'Winter'

number_hrizantems = int(input())
number_roses = int(input())
number_lale = int(input())
season = input()
holiday = input()

total_flowers = number_hrizantems + number_lale + number_roses
price_htizantem = 0
price_roses = 0
price_lale = 0
if season == 'Spring' or season == 'Summer':
    price_htizantem = 2
    price_roses = 4.10
    price_lale = 2.50
else:
    price_htizantem = 3.75
    price_roses = 4.50
    price_lale = 4.15

price_bucket = number_hrizantems * price_htizantem + number_roses * price_roses + number_lale * price_lale

if holiday == 'Y':
    price_bucket *= 1.15

elif holiday == 'N':
    price_bucket *= 1

if number_lale > 7 and season == 'Spring':
    price_bucket *= 0.95

if number_roses >= 10 and season == 'Winter':
    price_bucket *= 0.9

if total_flowers > 20:
    price_bucket *= 0.8

price_bucket = price_bucket + 2

print(f'{price_bucket:.2f}')

