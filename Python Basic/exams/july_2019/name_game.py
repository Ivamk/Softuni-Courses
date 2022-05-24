name = input()
numbers = len(name)
total_points_player = 0
best_player_name = ''
best_player_points = 0
while name != 'Stop':
    for sequence in range(numbers):
        current_number = int(input())
        if current_number == ord(name[sequence]):
            total_points_player += 10
        else:
            total_points_player += 2
    if total_points_player >= best_player_points:
        best_player_points = total_points_player
        best_player_name = name
    name = input()
    numbers = len(name)
    total_points_player = 0
print(f'The winner is {best_player_name} with {best_player_points} points!')
