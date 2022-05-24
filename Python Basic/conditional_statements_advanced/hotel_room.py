month = input()
number_stays = int(input())
price_per_night_studio = 0
price_per_night_apartment = 0
if month == 'May' or month == 'October':
    price_per_night_studio = 50
    price_per_night_apartment = 65
elif month == 'June' or month == 'September':
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70
elif month == 'July' or month == 'August':
    price_per_night_studio = 76
    price_per_night_apartment = 77

if 7 < number_stays <= 14 and (month == 'May' or month == 'October'):
    price_per_night_studio *= 0.95
elif number_stays > 14 and (month == 'May' or month == 'October'):
    price_per_night_studio *= 0.7
elif number_stays > 14 and (month == 'June' or month == 'September'):
    price_per_night_studio *= 0.8

if number_stays > 14:
    price_per_night_apartment *= 0.9

total_price_studio = number_stays * price_per_night_studio
total_price_apartment = number_stays * price_per_night_apartment

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')

