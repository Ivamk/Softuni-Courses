number_months = int(input())
total_cost = 0
cost_electricity = 0
other_costs = 0
for sequence in range(number_months):
    bill_electricity = float(input())
    cost_electricity += bill_electricity
    other_costs += (bill_electricity + 35) * 1.2
total_cost = cost_electricity + 35 * number_months + other_costs
average_total_costs = total_cost / number_months
print(f'Electricity: {cost_electricity:.2f} lv')
print(f'Water: {number_months * 20:.2f} lv')
print(f'Internet: {number_months * 15:.2f} lv')
print(f'Other: {other_costs:.2f} lv')
print(f'Average: {average_total_costs:.2f} lv')

