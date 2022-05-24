# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.

price_trip = float(input())
count_puzzles = int(input())
count_speaking_toy = int(input())
count_bear = int(input())
count_minion = int(input())
count_truck = int(input())

price_without_discount = count_puzzles * 2.60 + count_speaking_toy * 3 + count_bear * 4.10 + count_minion * 8.20 + count_truck * 2
ordered_toys = count_speaking_toy + count_truck + count_bear + count_minion + count_puzzles

if ordered_toys >= 50:
    price = price_without_discount - price_without_discount * 0.25
else:
    price = price_without_discount
final_profit = price * 0.9

price_left = final_profit - price_trip
price_left_minus = price_trip - final_profit

if price_left >= 0:
    print(f'Yes! {price_left:.2f} lv left.')
else:
    print(f'Not enough money! {price_left_minus:.2f} lv needed.')


