hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

time_of_exam = hour_of_exam * 60 + minutes_of_exam
time_of_arrival = hour_of_arrival * 60 + minutes_of_arrival

if time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print('On time')
elif time_of_arrival < time_of_exam - 30:
    print('Early')
elif time_of_arrival > time_of_exam:
    print('Late')

difference_minutes = abs(time_of_arrival - time_of_exam)
difference_hour = difference_minutes // 60
difference_minutes_left = difference_minutes % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f'{difference_minutes} minutes before the start')
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f'{difference_minutes} minutes after the start')
elif time_of_arrival <= time_of_exam - 60:
    print(f'{difference_hour}:{difference_minutes_left:02d} hours before the start')
elif time_of_arrival >= time_of_exam + 60:
    print(f'{difference_hour}:{difference_minutes_left:02d} hours after the start')

