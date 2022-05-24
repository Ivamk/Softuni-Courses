name_student = input()
current_class = 1
number_bad_grades = 0
sum_all_grades = 0
is_ejected = False
while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        number_bad_grades += 1
        if number_bad_grades > 1:
            is_ejected = True
            break
    else:
        sum_all_grades += current_grade
        current_class += 1
if is_ejected:
    print(f'{name_student} has been excluded at {current_class} grade')
else:
    average_grade = sum_all_grades / 12
    print(f'{name_student} graduated. Average grade: {average_grade:.2f}')

