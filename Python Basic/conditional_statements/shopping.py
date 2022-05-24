# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка.
# Видеокарта – 250 лв./бр.
# Процесор – 35% от цената на закупените видеокарти/бр.
# Рам памет – 10% от цената на закупените видеокарти/бр.

budget = float(input())
number_videocards = int(input())
number_processors = int(input())
number_ram = int(input())

price_videocards = 250
price_processor = price_videocards * number_videocards * 0.35
price_ram = price_videocards * number_videocards * 0.1

expenses = price_processor * number_processors + price_videocards * number_videocards + price_ram * number_ram

if number_videocards > number_processors:
    expenses = expenses * 0.85

difference = abs(budget - expenses)

if budget >= expenses:
    print(f'You have {difference:.2f} leva left!')

else:
    print(f'Not enough money! You need {difference:.2f} leva more!')

