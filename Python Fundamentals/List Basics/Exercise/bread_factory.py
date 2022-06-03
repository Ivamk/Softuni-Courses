working_day_events = input().split("|")
energy = 100
coins = 100
is_managed = True
for el in working_day_events:
    name_number = el.split("-")
    name = name_number[0]
    number = int(name_number[1])
    if name == "rest":
            temporary_energy = energy
            energy += number
            if energy > 100:
                energy = 100
            gained_energy = energy - temporary_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
    elif name == 'order':
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")
    else:
        if coins >= number:
            print(f'You bought {name}.')
            coins -= number
        else:
            print(f"Closed! Cannot afford {name}.")
            is_managed = False
            break
if is_managed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
