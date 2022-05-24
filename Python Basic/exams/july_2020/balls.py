import math

number_balls = int(input())
total_points = 0
red_point = 0
orange_point = 0
yellow_point = 0
white_point = 0
other_point = 0
black_devided = 0
for sequence in range(number_balls):
    current_colour = input()
    if current_colour == 'red':
        total_points += 5
        red_point += 1
    elif current_colour == 'orange':
        total_points += 10
        orange_point += 1
    elif current_colour == 'yellow':
        total_points += 15
        yellow_point += 1
    elif current_colour == 'white':
        total_points += 20
        white_point += 1
    elif current_colour == 'black':
        total_points /= 2
        total_points = math.floor(total_points)
        black_devided += 1
    else:
        other_point += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_point}")
print(f"Orange balls: {orange_point}")
print(f"Yellow balls: {yellow_point}")
print(f"White balls: {white_point}")
print(f"Other colors picked: {other_point}")
print(f"Divides from black balls: {black_devided}")
