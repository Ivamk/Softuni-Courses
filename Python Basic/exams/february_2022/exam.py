number_students = int(input())
fail_number = 0
average_number = 0
good_number = 0
excellent_number = 0
total_grades = 0
for sequence in range(number_students):
    grade = float(input())
    total_grades += grade
    if grade < 3:
        fail_number += 1
    elif 3 <= grade <= 3.99:
        average_number += 1
    elif 4 <= grade <= 4.99:
        good_number += 1
    elif grade >= 5:
        excellent_number += 1
percentage_excellent = excellent_number / number_students * 100
percentage_good = good_number / number_students * 100
percentage_average = average_number / number_students * 100
percentage_fail = fail_number / number_students * 100
percantage_average_grade = total_grades / number_students

print(f"Top students: {percentage_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_good:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_average:.2f}%")
print(f"Fail: {percentage_fail:.2f}%")
print(f"Average: {percantage_average_grade:.2f}")
