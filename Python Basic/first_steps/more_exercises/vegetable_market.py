price_vegetables = float(input())
price_fruits = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

income_bgn = price_vegetables * vegetables_kg + price_fruits * fruits_kg
fx_bgn_eur = 1.94
income_eur = income_bgn / fx_bgn_eur
print(f'{income_eur:.2f}')

