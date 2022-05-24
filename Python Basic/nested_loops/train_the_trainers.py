number = input()
name_presentation = input()
sum_points = 0
av_point_final = 0
projects = 0
while name_presentation != 'Finish':
    num_jury = int(number)
    projects += 1
    for sequence in range(1, num_jury + 1):
        points = float(input())
        sum_points += points
    av_point = sum_points / num_jury
    av_point_final += av_point
    print(f'{name_presentation} - {av_point:.2f}.')
    name_presentation = input()
    sum_points = 0
av_point_final = av_point_final / projects
print(f"Student's final assessment is {av_point_final:.2f}.")
