budget = float(input())
price_per_flour = float(input())
number_made_bread = 0
colored_eggs = 0
price_per_pack_eggs = 0.75 * price_per_flour
price_per_litre_milk = 1.25 * price_per_flour
price_per_bread = price_per_pack_eggs + price_per_flour + price_per_litre_milk/4
total_price = 0
while total_price < budget - price_per_bread:
    number_made_bread += 1
    colored_eggs += 3
    if number_made_bread % 3 == 0:
        colored_eggs -= number_made_bread - 2
    total_price = price_per_bread * number_made_bread
money_left = budget - total_price
print(f'You made {number_made_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
