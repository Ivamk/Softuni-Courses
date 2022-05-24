tax_over_20_kg = float(input())
weight_luggage = float(input())
days_to_departure = int(input())
number_luggage = int(input())

tax_luggage = 0
if weight_luggage < 10:
    tax_luggage = tax_over_20_kg * 0.2
elif 10 <= weight_luggage <= 20:
    tax_luggage = tax_over_20_kg * 0.5
elif weight_luggage > 20:
    tax_luggage = tax_over_20_kg * 1

if days_to_departure < 7:
    tax_luggage = tax_luggage * 1.4
elif 7 <= days_to_departure <= 30:
    tax_luggage = tax_luggage * 1.15
elif days_to_departure > 30:
    tax_luggage = tax_luggage * 1.1

total_tax_luggage = tax_luggage * number_luggage

print(f'The total price of bags is: {total_tax_luggage:.2f} lv.')
