import math

number_tournaments = int(input())
start_points = int(input())
sum_of_points = 0
win_tournament = 0
total_points = 0
for sequence in range(number_tournaments):
    final_stage_reached = input()
    if final_stage_reached == 'W':
        sum_of_points += 2000
        win_tournament += 1
    elif final_stage_reached == 'F':
        sum_of_points += 1200
    elif final_stage_reached == 'SF':
        sum_of_points += 720
    total_points = start_points + sum_of_points
average_points = sum_of_points / number_tournaments
win_tournament_percentage = win_tournament / number_tournaments * 100
print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{win_tournament_percentage:.2f}%')
