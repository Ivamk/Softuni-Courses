volume_pool = int(input())
volume_per_hour_first = int(input())
volume_per_hour_second = int(input())
hours_missing = float(input())

debit_first_tube = volume_per_hour_first * hours_missing
debit_second_tube = volume_per_hour_second * hours_missing
full_littres_pool = debit_first_tube + debit_second_tube

if full_littres_pool <= volume_pool:
    occupancy_percentage = full_littres_pool / volume_pool * 100
    first_tube_percentage = debit_first_tube / full_littres_pool * 100
    second_tube_percentage = debit_second_tube / full_littres_pool * 100
    print(f'The pool is {occupancy_percentage:.2f}% full. Pipe 1: {first_tube_percentage:.2f}%. Pipe 2: {second_tube_percentage:.2f}%.')
else:
    overflow = abs (full_littres_pool - volume_pool)
    print(f'For {hours_missing} hours the pool overflows with {overflow:.2f} liters.')




