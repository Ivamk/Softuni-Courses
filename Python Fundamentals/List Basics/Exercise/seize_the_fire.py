fire = input().split('#')
water = int(input())
effort = 0
total_fire = 0
final_list = []
is_fire = True
for el in fire:
    level_value = el.split('=')
    type_of_fire = level_value[0]
    needed_water = int(level_value[1])
    if type_of_fire == 'High ' and water - needed_water >= 0:
        if 81 <= needed_water <= 125:
            water -= needed_water
            effort += needed_water * 0.25
            total_fire += needed_water
            final_list.append(needed_water)
    elif type_of_fire == 'Medium ' and water - needed_water >= 0:
        if 51 <= needed_water <= 80:
            water -= needed_water
            effort += needed_water * 0.25
            total_fire += needed_water
            final_list.append(needed_water)
    elif type_of_fire == 'Low ' and water - needed_water >= 0:
        if 1 <= needed_water <= 50:
            water -= needed_water
            effort += needed_water * 0.25
            total_fire += needed_water
            final_list.append(needed_water)
print("Cells:")
for elem in final_list:
    print(f"- {elem}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
