money_heritage = float(input())
year_of_dead = int(input())
spent_money = 0
for sequence in range(1800, year_of_dead + 1):
    if sequence % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + 50 * (18 + (sequence - 1800))

diff = abs(spent_money - money_heritage)
if money_heritage >= spent_money:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')
