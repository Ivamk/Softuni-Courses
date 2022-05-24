from math import ceil

height = int(input())
weight = int(input())
percentage_doors = int(input())
to_be_painted = height * weight * 4
to_be_painted *= (1 - percentage_doors / 100)
to_be_painted = ceil(to_be_painted)
command = input()
is_painted = False
while command != 'Tired!':
    littres = int(command)
    to_be_painted -= littres
    if to_be_painted <= 0:
        is_painted = True
        break
    command = input()
if command == 'Tired!':
    print(f'{to_be_painted} quadratic m left.')
if is_painted and to_be_painted < 0:
    print(f'All walls are painted and you have {abs(to_be_painted)} l paint left!')
if is_painted and to_be_painted == 0:
    print(f'All walls are painted! Great job, Pesho!')

