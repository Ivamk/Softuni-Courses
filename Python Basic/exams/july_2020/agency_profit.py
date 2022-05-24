name_air_company = input()
number_tickets_adults = int(input())
number_tickets_children = int(input())
net_price_adult = float(input())
service_tax = float(input())

net_price_children = net_price_adult * 0.3

total_income = number_tickets_adults * (net_price_adult + service_tax) + number_tickets_children * (net_price_children + service_tax)

profit = total_income * 0.2

print(f'The profit of your agency from {name_air_company} tickets is {profit:.2f} lv.')
