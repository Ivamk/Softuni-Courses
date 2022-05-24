# 1.	Плод - текст с възможности: "Watermelon", "Mango", "Pineapple" или "Raspberry"
# 2.	Размерът на сета - текст с възможности: "small" или "big"
# 3.	Брой на поръчаните сетове - цяло число в интервала [1 … 10000]
fruit = input()
type_set = input()
number_sets = int(input())
price_per_number = 0
price_per_set = 0
if type_set == 'small':
    if fruit == 'Watermelon':
        price_per_number = 56
    elif fruit == 'Mango':
        price_per_number = 36.66
    elif fruit == 'Pineapple':
        price_per_number = 42.10
    elif fruit == 'Raspberry':
        price_per_number = 20
    price_per_set = price_per_number * 2
elif type_set == 'big':
    if fruit == 'Watermelon':
        price_per_number = 28.70
    elif fruit == 'Mango':
        price_per_number = 19.60
    elif fruit == 'Pineapple':
        price_per_number = 24.80
    elif fruit == 'Raspberry':
        price_per_number = 15.20
    price_per_set = price_per_number * 5
price_order = number_sets * price_per_set
if 400 <= price_order <= 1000:
    price_order *= 0.85
elif price_order > 1000:
    price_order *= 0.5
print(f"{price_order:.2f} lv.")
