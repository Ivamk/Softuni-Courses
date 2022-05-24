old_record = float(input())
distance = float(input())
time_per_meter = float(input())

delay = distance // 15
time_all = distance * time_per_meter + delay * 12.5

difference = abs(time_all - old_record)

if time_all >= old_record:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
if time_all < old_record:
    print(f'Yes, he succeeded! The new world record is {time_all:.2f} seconds.')
