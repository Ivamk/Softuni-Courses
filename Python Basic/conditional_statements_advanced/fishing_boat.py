budget = int(input())
season = input()
number_fishermen = int(input())
price_rent = 0

if season == 'Spring':
    price_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    price_rent = 4200
elif season == 'Winter':
    price_rent = 2600

if number_fishermen <= 6:
    price_rent *= 0.9
elif 7 <= number_fishermen <= 11:
    price_rent *= 0.85
elif number_fishermen >= 12:
    price_rent *= 0.75

if number_fishermen % 2 == 0 and not season == 'Autumn':
    price_rent *= 0.95

difference = abs(budget - price_rent)

if budget >= price_rent:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')

