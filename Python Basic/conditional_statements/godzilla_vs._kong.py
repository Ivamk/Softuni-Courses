budget = float(input())
number_statists = int(input())
price_clothes_per_statists = float(input())
decor = budget * 0.1
if number_statists > 150:
    price_clothes_per_statists = price_clothes_per_statists * 0.9

expenses = number_statists * price_clothes_per_statists + decor

difference = abs(expenses - budget)

if expenses <= budget:
    print("Action!")
    print(f'Wingard starts filming with {difference:.2f} leva left.')
if expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
