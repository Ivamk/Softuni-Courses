people = int(input())
season = input()
price = 0
if season == 'spring':
    if people <= 5:
        price = 50.00
    elif people > 5:
        price = 48.00
elif season == 'summer':
    if people <= 5:
        price = 48.50
    elif people > 5:
        price = 45.00
elif season == 'autumn':
    if people <= 5:
        price = 60.00
    elif people > 5:
        price = 49.50
elif season == 'winter':
    if people <= 5:
        price = 86.00
    elif people > 5:
        price = 85.00
total_price = people * price
if season == 'summer':
    total_price *= 0.85
elif season == 'winter':
    total_price *= 1.08
print(f'{total_price:.2f} leva.')
