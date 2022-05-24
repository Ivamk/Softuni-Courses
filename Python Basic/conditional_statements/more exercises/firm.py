needed_time = int(input())
available_days = int(input())
number_employees = int(input())

working_regular_hours = available_days * 0.9 * 8
working_extraordinary_hours = number_employees * 2 * available_days

total_working_hours = working_regular_hours + working_extraordinary_hours

total_working_hours = total_working_hours // 1

difference = abs(total_working_hours - needed_time)
if needed_time <= total_working_hours:
    print(f'Yes!{difference:.0f} hours left.')
else:
    print(f'Not enough time!{difference:.0f} hours needed.')