budget = float(input())
season = input()
accomodation = ' '
place = ' '
price = 0
if budget <= 1000:
    accomodation = 'Camp'
    if season == "Summer":
        place = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        place = "Morocco"
        price = budget * 0.45

elif budget > 1000 and budget <= 3000:
    accomodation = 'Hut'
    if season == "Summer":
        place = 'Alaska'
        price = budget * 0.8
    elif season == 'Winter':
        place = "Morocco"
        price = budget * 0.6
else:
    price = budget * 0.9
    accomodation = 'Hotel'
    if season == "Summer":
        place = 'Alaska'
    elif season == 'Winter':
        place = "Morocco"

print(f'{place} - {accomodation} - {price:.2f}')

