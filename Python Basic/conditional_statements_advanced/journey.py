budget = float(input())
season = input()
place = ' '
destination = ' '
spended_money = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        spended_money = budget * 0.3
    elif season == 'winter':
        spended_money = budget * 0.7
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spended_money = budget * 0.4
    elif season == 'winter':
        spended_money = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    spended_money = budget * 0.9

if destination == 'Europe':
    place = 'Hotel'

if season == 'summer' and not destination == 'Europe':
    place = 'Camp'
elif season == 'winter':
    place = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{place} - {spended_money:.2f}')
