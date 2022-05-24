# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая

number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegiterian_menus = int(input())

price_per_chichen_menu = 10.35
price_per_fish_menu = 12.40
price_per_vegiterian_menu = 8.15

price_without_desert = number_chicken_menus * price_per_chichen_menu + \
                       number_fish_menus * price_per_fish_menu + \
                       number_vegiterian_menus * price_per_vegiterian_menu

price_desert = price_without_desert * 0.2

price_with_desert = price_without_desert + price_desert

total_price = price_with_desert + 2.50

print(total_price)
