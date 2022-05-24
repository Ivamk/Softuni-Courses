record_in_seconds = float(input())
distance_metres = float(input())
sec_per_meter = float(input())
current_seconds = distance_metres * sec_per_meter
additional_time = (distance_metres // 50) * 30
total_time = current_seconds + additional_time
difference = abs(total_time - record_in_seconds)
if total_time < record_in_seconds:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {difference:.2f} seconds slower.')
