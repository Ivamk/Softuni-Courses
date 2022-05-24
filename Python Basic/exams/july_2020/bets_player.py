command = input()
best_goals = 0
best_player = ''

while command != 'END':
    is_hatrick = False
    name_player = command
    current_goals = int(input())
    if current_goals > best_goals:
        best_goals = current_goals
        best_player = name_player
    if current_goals >= 3:
        is_hatrick = True
    if current_goals >= 10:
        break
    command = input()
print(f"{best_player} is the best player!")
if is_hatrick:
    print(f'He has scored {best_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_goals} goals.')