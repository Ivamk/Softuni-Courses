from math import pi

figure = input()
side_a = float(input())
area_figure = 0

if figure == 'square':
    area_figure = side_a ** 2
if figure == 'rectangle':
    side_b = float(input())
    area_figure = side_a * side_b
if figure == 'circle':
    area_figure = pi * (side_a ** 2)
if figure == 'triangle':
    hight = float (input())
    area_figure = side_a * hight / 2

print(f'{area_figure:.3f}')


