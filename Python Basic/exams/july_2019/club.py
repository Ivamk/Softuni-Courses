profit_to_reach = float(input())
name_cocktail = input()
total_profit = 0
is_target = False
while name_cocktail != 'Party!':
    current_number_cocktails = int(input())
    price_cocktail = len(name_cocktail)
    price_order = current_number_cocktails * price_cocktail
    if price_order % 2 != 0:
        price_order *= 0.75
    total_profit += price_order
    if total_profit >= profit_to_reach:
        is_target = True
        break
    name_cocktail = input()
    difference = abs(profit_to_reach - total_profit)
    if name_cocktail == 'Party!':
        print(f'We need {difference:.2f} leva more.')

if is_target:
    print(f'Target acquired.')
print(f'Club income - {total_profit:.2f} leva.')
