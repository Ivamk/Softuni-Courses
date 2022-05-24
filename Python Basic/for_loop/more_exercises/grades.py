number_students = int(input())
estimation_fail = 0
estimation_average = 0
estimation_good = 0
estimation_top = 0
total_evaluation = 0
for sequence in range(number_students):
    evaluation_exam = float(input())
    total_evaluation += evaluation_exam
    if 2.00 <= evaluation_exam <= 2.99:
        estimation_fail += 1
    elif 3.00 <= evaluation_exam <= 3.99:
        estimation_average += 1
    elif 4.00 <= evaluation_exam <= 4.99:
        estimation_good += 1
    elif 5.00 <= evaluation_exam:
        estimation_top += 1
top_students = estimation_top / number_students * 100
good_students = estimation_good / number_students * 100
average_students = estimation_average / number_students * 100
failed_students = estimation_fail / number_students * 100
average_evaluation = total_evaluation / number_students
print(f'Top students: {top_students:.2f}%')
print(f'Between 4.00 and 4.99: {good_students:.2f}%')
print(f'Between 3.00 and 3.99: {average_students:.2f}%')
print(f'Fail: {failed_students:.2f}%')
print(f'Average: {average_evaluation:.2f}')
