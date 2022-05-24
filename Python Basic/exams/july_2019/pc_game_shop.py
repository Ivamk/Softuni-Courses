number_sold_games = int(input())
counter_heartstone = 0
counter_fornite = 0
counter_overwatch = 0
counter_others = 0
for sequence in range(number_sold_games):
    name = input()
    if name == 'Hearthstone':
        counter_heartstone += 1
    elif name == 'Fornite':
        counter_fornite += 1
    elif name == 'Overwatch':
        counter_overwatch += 1
    else:
        counter_others += 1
percentage_heratstone = counter_heartstone / number_sold_games * 100
percentage_fornite = counter_fornite / number_sold_games * 100
percentage_overwatch = counter_overwatch / number_sold_games * 100
percentage_others = counter_others / number_sold_games * 100

print(f'Hearthstone - {percentage_heratstone:.2f}%')
print(f'Fornite - {percentage_fornite:.2f}%')
print(f'Overwatch - {percentage_overwatch:.2f}%')
print(f'Others - {percentage_others:.2f}%')
