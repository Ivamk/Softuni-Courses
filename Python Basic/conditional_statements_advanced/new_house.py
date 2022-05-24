kind_of_flowers = input()
number_flower = int(input())
budget = int(input())
price = 0
if kind_of_flowers == 'Roses':
    if number_flower <= 80:
        price = 5
    else:
        price = 5 * 0.9
elif kind_of_flowers == 'Dahlias':
    if number_flower <= 90:
        price = 3.80
    else:
        price = 3.80 * 0.85
elif kind_of_flowers == 'Tulips':
    if number_flower <= 80:
        price = 2.80
    else:
        price = 2.80 * 0.85
elif kind_of_flowers == 'Narcissus':
    if number_flower >= 120:
        price = 3
    else:
        price = 3 * 1.15
elif kind_of_flowers == 'Gladiolus':
    if number_flower >= 80:
        price = 2.5
    else:
        price = 2.50 * 1.20

total_price = price * number_flower
difference = abs(total_price - budget)

if budget >= total_price:
    print(f'Hey, you have a great garden with {number_flower} {kind_of_flowers} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
