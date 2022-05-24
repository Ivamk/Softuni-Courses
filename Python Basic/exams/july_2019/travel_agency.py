name_city = input()
package = input()
vip = input()
days_stay = int(input())
price_per_day = 0
vip_discount = 0
is_correct = True
if name_city == 'Bansko' or name_city == 'Borovets':
    if package == 'withEquipment':
        price_per_day = 100
        vip_discount = 10
    elif package == 'noEquipment':
        price_per_day = 80
        vip_discount = 5
elif name_city == 'Varna' or name_city == 'Burgas':
    if package == 'withBreakfast':
        price_per_day = 130
        vip_discount = 12
    elif package == 'noBreakfast':
        price_per_day = 100
        vip_discount = 7
else:
    is_correct = False
    print(f'Invalid input!')
if days_stay > 7:
    days_stay = days_stay - 1
if vip == 'yes':
    total_price = price_per_day * days_stay - price_per_day * days_stay * vip_discount / 100
elif vip == 'no':
    total_price = price_per_day * days_stay
else:
    is_correct = False
    print(f'Invalid input!')
if days_stay < 1:
    is_correct = False
    print(f'Days must be positive number!')
if is_correct:
    print(f'The price is {total_price:.2f}lv! Have a nice time!')