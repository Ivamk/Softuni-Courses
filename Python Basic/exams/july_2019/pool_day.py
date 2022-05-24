from math import ceil

number_people = int(input())
price_entrance = float(input())
price_leg = float(input())
price_umbrella = float(input())

total_price_entrance = number_people * price_entrance
total_price_legs = ceil(0.75 * number_people) * price_leg

total_price_umbrella = ceil(number_people * 0.5) * price_umbrella
total_price = total_price_umbrella + total_price_legs + total_price_entrance

print(f'{total_price:.2f} lv.')