name_of_actor = input()
points_from_academy = float(input())
number_jury = int(input())
sum_of_points = 0
for sequence in range (number_jury):
    name_of_jury = input()
    points_from_jury = float(input())
    sum_of_points += (len(name_of_jury) * points_from_jury / 2)
    total_points = sum_of_points + points_from_academy
    if total_points > 1250.5:
        break
needed_points = 1250.5 - total_points
if total_points > 1250.5:
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {name_of_actor} you need {needed_points:.1f} more!')




