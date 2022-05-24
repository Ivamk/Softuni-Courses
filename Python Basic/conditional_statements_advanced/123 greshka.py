budget = float(input())
season = input()
price = 0
destination = ""
type_of_journey = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_journey = "Camp"
        price = budget * 0.30
    elif season == "Winter":
        type_of_journey = "Hotel"
        price = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "Summer":
        type_of_journey = "Camp"
        price = budget * 0.40
    elif season == "Winter":
        type_of_journey = "Hotel"
        price = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    type_of_journey = "Hotel"
    price = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{type_of_journey} - {price:.2f}')