# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)
# •	Брой пакети химикали - цяло число в интервала [0...100]
# •	Брой пакети маркери - цяло число в интервала [0...100]
# •	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# •	Процент намаление - цяло число в интервала [0...100]

package_pens = int(input())
package_markers = int(input())
cleaning_litres = int(input())
percentage_discount = int(input())

price_pens = 5.80
price_markers = 7.20
price_cleaning = 1.20
total_price = package_pens * price_pens + \
              package_markers * price_markers + \
              cleaning_litres * price_cleaning
discount_absolute = percentage_discount / 100
final_price = total_price - total_price * discount_absolute

print(final_price)
