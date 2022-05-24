budget = float(input())
season = input()
category = ' '
car = ' '
price = 0
if budget <= 100:
    category = 'Economy class'
    if season == "Summer":
        car = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car = "Jeep"
        price = budget * 0.65

elif budget > 100 and budget <= 500:
    category = 'Compact class'
    if season == "Summer":
        car = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car = "Jeep"
        price = budget * 0.8
else:
    category = 'Luxury class'
    car = 'Jeep'
    price = budget * 0.9

print(category)
print(f'{car} - {price:.2f}')