x_weight = float(input())
y_lenght = float(input())
h_height = float(input())

# Green painting
front_wall = x_weight * x_weight - 1.2 * 2
back_wall = x_weight * x_weight
side_wall = x_weight * y_lenght - 1.5*1.5
area_green_painting = front_wall + back_wall + 2 * side_wall
green_painting_littres = area_green_painting / 3.4

# red painting
rectangular_side = x_weight * y_lenght
triangle_side = x_weight * h_height / 2
area_red_painting = 2 * rectangular_side + 2 * triangle_side
red_painting_littres = area_red_painting / 4.3

print(f'{green_painting_littres:.2f}')
print(f'{red_painting_littres:.2f}')
