# Цената на един кв. м. е 7.61 лв със ДДС
# "The final price is: {крайна цена на услугата} lv."
# "The discount is: {отстъпка} lv."

plot_sq_m = float(input())

total_price = plot_sq_m * 7.61
discount_price = total_price * 0.18
final_price = total_price - discount_price

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount_price} lv.')
