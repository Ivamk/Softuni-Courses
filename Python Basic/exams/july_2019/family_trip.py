budget = float(input())
number_nights = int(input())
price_per_nights = float(input())
percentage_extra_expenses = int(input())
if number_nights > 7:
    price_per_nights = 0.95 * price_per_nights
price_trip = number_nights * price_per_nights + percentage_extra_expenses * budget / 100
difference = abs(price_trip - budget)
if budget >= price_trip:
    print(f'Ivanovi will be left with {difference:.2f} leva after vacation.')
else:
    print(f"{difference:.2f} leva needed.")
