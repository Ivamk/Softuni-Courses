number_pages = int(input())
pages_per_hour = int(input())
number_days = int(input())

needed_hours = number_pages / pages_per_hour
hours_per_day = needed_hours / number_days

print(int(hours_per_day))