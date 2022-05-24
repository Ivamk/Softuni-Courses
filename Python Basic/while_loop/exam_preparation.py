number_unsatisfactory_grades = int(input())
command = input()
sum_all_problems = 0
sum_all_grades = 0
last_problem = ''
number_bad_grades = 0
if_enough = True
while command != 'Enough':
    current_grade = float(input())
    last_problem = command
    sum_all_grades += current_grade
    sum_all_problems += 1
    if current_grade <= 4:
        number_bad_grades += 1
        if number_bad_grades == number_unsatisfactory_grades:
            if_enough = False
            break
    command = input()
if not if_enough:
    print(f'You need a break, {number_bad_grades} poor grades.')
else:
    average_score = sum_all_grades / sum_all_problems
    print(f'Average score: {average_score:.2f}\nNumber of problems: {sum_all_problems}\nLast problem: {last_problem}')
