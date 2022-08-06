import math

number_electrons = int(input())
used_electrons = 0
filled_shels = []
step_electrons = 1
while number_electrons > 0:
    if number_electrons > 2 * pow(step_electrons, 2):
        used_electrons = 2 * pow(step_electrons, 2)
        filled_shels.append(used_electrons)
        number_electrons -= used_electrons
    else:
        filled_shels.append(number_electrons)
        number_electrons = 0
    step_electrons += 1
print(filled_shels)

