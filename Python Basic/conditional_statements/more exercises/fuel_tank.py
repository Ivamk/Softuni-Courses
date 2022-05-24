type_fuel = input()
liters_left = float(input())

if type_fuel == 'Diesel' or type_fuel == 'Gasoline' or type_fuel == 'Gas':
    type_fuel = type_fuel.lower()
    if liters_left < 25:
        print(f'Fill your tank with {type_fuel}!')
    else:
        print(f'You have enough {type_fuel}.')

else:
    print('Invalid fuel!')
