# Бензин – 2.22 лева за един литър,
# Дизел – 2.33 лева за един литър
# Газ – 0.93 лева за литър

# отстъпки - 18 ст. за литър бензин, 12 ст. за литър дизел и 8 ст. за литър газ.

type_fuel = input()
quantity_fuel = float(input())
club_card = input()

if club_card == 'Yes':
    if type_fuel == 'Gasoline':
        total_price = quantity_fuel * (2.22-0.18)
        if quantity_fuel >= 20 and quantity_fuel <= 25:
            total_price = total_price * 0.92
        elif quantity_fuel > 25:
            total_price = total_price * 0.90
    elif type_fuel == 'Gas':
        total_price = quantity_fuel * (0.93 - 0.08)
        if quantity_fuel >= 20 and quantity_fuel <= 25:
            total_price = total_price * 0.92
        elif quantity_fuel > 25:
            total_price = total_price * 0.90
    elif type_fuel == 'Diesel':
        total_price = quantity_fuel * (2.33 - 0.12)
        if quantity_fuel >= 20 and quantity_fuel <= 25:
            total_price = total_price * 0.92
        elif quantity_fuel > 25:
            total_price = total_price * 0.90

elif club_card == 'No':
    if type_fuel == 'Gasoline':
        total_price = quantity_fuel * 2.22
        if quantity_fuel >= 20 and quantity_fuel <= 25:
            total_price = total_price * 0.92
        elif quantity_fuel > 25:
            total_price = total_price * 0.90
    elif type_fuel == 'Gas':
        total_price = quantity_fuel * 0.93
        if quantity_fuel >= 20 and quantity_fuel <= 25:
            total_price = total_price * 0.92
        elif quantity_fuel > 25:
            total_price = total_price * 0.90
    elif type_fuel == 'Diesel':
        total_price = quantity_fuel * 2.33
        if quantity_fuel >= 20 and quantity_fuel <= 25:
            total_price = total_price * 0.92
        elif quantity_fuel > 25:
            total_price = total_price * 0.90

print(f'{total_price:.2f} lv.')
