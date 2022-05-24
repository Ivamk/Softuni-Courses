from math import ceil, floor

# Магнолии – 3.25 лева
# Зюмбюли – 4 лева
# Рози – 3.50 лева
# Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци.

number_magnolii = int(input())
number_ziumbiul = int(input())
number_roses = int(input())
number_cactus = int(input())
price_present = float(input())

price_bouquet = number_magnolii * 3.25 + number_ziumbiul * 4 + number_roses * 3.50 + number_cactus * 8
final_price_bouquet = price_bouquet * 0.95
difference = abs(final_price_bouquet - price_present)
if final_price_bouquet >= price_present:
    print(f'She is left with {floor(difference)} leva.')
else:
    print(f'She will have to borrow {ceil(difference)} leva.')
