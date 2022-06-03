events = input().split('|')
energy = 100
coins = 100
closed = False
for event in events:
    action, numbers = event.split('-')
    numbers = int(numbers)
    if action == 'rest':
        temp = energy + numbers
        if temp >= 100:
            print(f'You gained {100 - energy} energy.')
        else:
            print(f'You gained {numbers} energy.')
        energy += numbers

        if energy > 100:
            energy = 100

        print(f'Current energy: {energy}.')

    elif action == 'order':
        if energy < 30:
            energy += 50
            print(f"You had to rest!")
            continue
        coins += numbers
        energy -= 30
        print(f"You earned {numbers} coins.")

    else:
        if coins >= numbers:
            coins -= numbers
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            closed = True
            break

if not closed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")