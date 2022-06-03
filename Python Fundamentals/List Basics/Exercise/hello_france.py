item_list = input().split("|")
budget = float(input())
higher_prices_list = []
max_price_clothes = 50
max_price_shoes = 35
max_price_accessories = 20.50
profit = 0
sum_of_all_new_prices = 0
for element in item_list:
    temp_item = element.split("->")
    temp_product = temp_item[0]
    temp_price = float(temp_item[1])
    if budget >= temp_price:
        if (temp_product == "Clothes" and temp_price <= max_price_clothes) or (temp_product == "Shoes" and temp_price <= max_price_shoes)\
                or (temp_product == "Accessories" and temp_price <= max_price_accessories):
            budget -= temp_price
            higher_prices_list.append(temp_price*1.4)
            profit += temp_price * 0.4
        else:
            continue

final_sum = sum(higher_prices_list) + budget

for el in higher_prices_list:
    print(f"{el:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if final_sum >= 150:
    print('Hello, France!')
else:
    print("Not enough money.")
