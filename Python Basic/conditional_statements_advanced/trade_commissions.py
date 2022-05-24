city = input()
volume_sell = float(input())
commission = 0
city_is_valid = True
volume_sell_is_valid = True

if 0 <= volume_sell <= 500:
    if city == 'Sofia':
        commission = 0.05
    elif city == 'Varna':
        commission = 0.045
    elif city == 'Plovdiv':
        commission = 0.055
    else:
        city_is_valid = False
elif 500 < volume_sell <= 1000:
    if city == 'Sofia':
        commission = 0.07
    elif city == 'Varna':
        commission = 0.075
    elif city == 'Plovdiv':
        commission = 0.08
    else:
        city_is_valid = False
elif 1000 < volume_sell <= 10000:
    if city == 'Sofia':
        commission = 0.08
    elif city == 'Varna':
        commission = 0.1
    elif city == 'Plovdiv':
        commission = 0.12
    else:
        city_is_valid = False
elif volume_sell > 10000:
    if city == 'Sofia':
        commission = 0.12
    elif city == 'Varna':
        commission = 0.13
    elif city == 'Plovdiv':
        commission = 0.145
    else:
        city_is_valid = False
else:
    volume_sell_is_valid = False
if city_is_valid and volume_sell_is_valid:
    income = commission * volume_sell
    print(f'{income:.2f}')
else:
    print('error')
    