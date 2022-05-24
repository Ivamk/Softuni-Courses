current_age = int(input())
laundry_price = float(input())
price_per_toy = int(input())
sum_money = 0
number_toys = 0
total_sum = 0
for sequence in range(1, current_age + 1):
    if sequence % 2 == 0:
        sum_money += 10
        total_sum += sum_money - 1
    else:
        number_toys += 1
total_sum += number_toys * price_per_toy
difference = abs(total_sum - laundry_price)
if total_sum >= laundry_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
