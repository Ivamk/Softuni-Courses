budget = float(input())
category = input()
number_people = int(input())

price_ticket = 0
transport = 0
if category == 'VIP':
    price_ticket = 499.99
elif category == 'Normal':
    price_ticket = 249.99

if 1 <= number_people <= 4:
    transport = budget * 0.75
elif 5 <= number_people <= 9:
    transport = budget * 0.6
elif 10 <= number_people <= 24:
    transport = budget * 0.5
elif 25 <= number_people <= 49:
    transport = budget * 0.4
elif 50 <= number_people:
    transport = budget * 0.25

total_price_for_tickets = number_people * price_ticket
rest_of_budget = budget - transport
difference = abs (rest_of_budget - total_price_for_tickets)

if rest_of_budget >= total_price_for_tickets:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')

