from math import floor, ceil

plot_area = int(input())
crop_grape_per_meter = float(input())
needed_liters_wine = int(input())
number_workers = int(input())

total_crop = plot_area * crop_grape_per_meter
crop_for_wine = total_crop * 0.4
liters_wine_realized = crop_for_wine / 2.5

difference = abs(needed_liters_wine - liters_wine_realized)
wine_per_worker = difference / number_workers

if liters_wine_realized < needed_liters_wine:
    print(f'It will be a tough winter! More {floor(difference)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(liters_wine_realized)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.')
