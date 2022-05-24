number_cargo = int(input())
total_price = 0
total_tonnes = 0
p_microbus = 0
p_truck = 0
p_train = 0
for sequence in range(number_cargo):
    tonnes_cargo = int(input())
    total_tonnes += tonnes_cargo
    if tonnes_cargo <= 3:
        total_price += tonnes_cargo * 200
        p_microbus += tonnes_cargo
    elif 4 <= tonnes_cargo <= 11:
        total_price += tonnes_cargo * 175
        p_truck += tonnes_cargo
    else:
        total_price += tonnes_cargo * 120
        p_train += tonnes_cargo

average_price_per_ton = total_price / total_tonnes
percentage_microbus = p_microbus / total_tonnes * 100
percentage_truck = p_truck / total_tonnes * 100
percentage_train = p_train / total_tonnes * 100
print(f'{average_price_per_ton:.2f}')
print(f'{percentage_microbus:.2f}%')
print(f'{percentage_truck:.2f}%')
print(f'{percentage_train:.2f}%')

