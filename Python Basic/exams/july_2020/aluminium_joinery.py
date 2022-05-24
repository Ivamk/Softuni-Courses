number_joinery = int(input())
type_joinery = input()
type_delivery = input()

price_per_joinery = 0
number_joinery_is_valid = True
if number_joinery > 10:
    if type_joinery == '90X130':
        price_per_joinery = 110
        if 30 < number_joinery <= 60:
            price_per_joinery *= 0.95
        elif number_joinery > 60:
            price_per_joinery *= 0.92
    elif type_joinery == '100X150':
        price_per_joinery = 140
        if 40 < number_joinery <= 80:
            price_per_joinery *= 0.94
        elif number_joinery > 80:
            price_per_joinery *= 0.90
    elif type_joinery == '130X180':
        price_per_joinery = 190
        if 20 < number_joinery <= 50:
            price_per_joinery *= 0.93
        elif number_joinery > 50:
            price_per_joinery *= 0.88
    elif type_joinery == '200X300':
        price_per_joinery = 250
        if 25 < number_joinery <= 50:
            price_per_joinery *= 0.91
        elif number_joinery > 50:
            price_per_joinery *= 0.86
else:
    number_joinery_is_valid = False
total_price = number_joinery * price_per_joinery

if type_delivery == 'With delivery':
    total_price += 60

if number_joinery > 99:
    total_price *= 0.96
if number_joinery_is_valid:
    print(f'{total_price:.2f} BGN')
else:
    print('Invalid order')

    



