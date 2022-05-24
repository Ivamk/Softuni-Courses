season = input()
type_group = input()
number_students = int(input())
number_nights = int(input())
price_per_night = 0
sport = ' '
if season == 'Winter':
    if type_group == 'girls':
        price_per_night = 9.6
        sport = 'Gymnastics'
    elif type_group == 'boys':
        price_per_night = 9.6
        sport = 'Judo'
    elif type_group == 'mixed':
        price_per_night = 10
        sport = 'Ski'
elif season == 'Spring':
    if type_group == 'girls':
        price_per_night = 7.2
        sport = 'Athletics'
    elif type_group == 'boys':
        price_per_night = 7.2
        sport = 'Tennis'
    elif type_group == 'mixed':
        price_per_night = 9.5
        sport = 'Cycling'
elif season == 'Summer':
    if type_group == 'girls':
        price_per_night = 15
        sport = 'Volleyball'
    elif type_group == 'boys':
        price_per_night = 15
        sport = 'Football'
    elif type_group == 'mixed':
        price_per_night = 20
        sport = 'Swimming'

price_all_nights = price_per_night * number_nights * number_students

if number_students >=10 and number_students < 20:
    price_all_nights *= 0.95
elif number_students >=20 and number_students < 50:
    price_all_nights *= 0.85
elif number_students >=50:
    price_all_nights *= 0.5

print(f'{sport} {price_all_nights:.2f} lv.')
