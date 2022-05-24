# една опаковка храна за кучета е на цена 2.50 лв,
# а опаковка храна за котки струва 4 лв.
# 28.5 lv.

count_dog_packages = int(input())
count_cat_packaged = int(input())
price_all_dog = count_dog_packages * 2.50
price_all_cat = count_cat_packaged * 4
total_price = price_all_dog + price_all_cat

print(f'{total_price} lv.')

