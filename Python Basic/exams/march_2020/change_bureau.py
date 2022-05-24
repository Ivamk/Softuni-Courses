# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.



bitcoins = int(input())
chinese_jan = float(input())
commission = float(input())
one_bitcoin = 1168
one_chinese_jan = 0.15 * 1.76
total_price_euro = ((one_bitcoin * bitcoins) + (one_chinese_jan * chinese_jan)) / 1.95
commission_to_add = total_price_euro * commission / 100
result = total_price_euro - commission_to_add
print(f'{result:.2f}')

