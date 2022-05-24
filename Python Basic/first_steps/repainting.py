# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон,
# разбира се и 0.40 лв. за торбички.
# Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали

nylon_sq_m = int(input())
painting_littres = int(input())
detergent_littres = int(input())
needed_hours = int (input())

price_nylon_per_sqm = 1.50
price_painting_per_littre = 14.50
price_detergent_per_littre = 5.00
price_bags = 0.40

total_price_materials = (nylon_sq_m + 2) * price_nylon_per_sqm + \
                        (painting_littres * 1.1) * price_painting_per_littre + \
                        detergent_littres * price_detergent_per_littre + price_bags

maistor_per_hour = total_price_materials * 0.3

total_price_maistor = maistor_per_hour * needed_hours

total_price = total_price_materials + total_price_maistor

print(total_price)