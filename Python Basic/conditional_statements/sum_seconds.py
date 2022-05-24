first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time

hours = total_time // 60
minutes = total_time % 60
if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')


