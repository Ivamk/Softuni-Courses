from math import ceil

name_serial = input()
time_epizode = int(input())
time_break = int(input())

time_to_lunch = time_break / 8
time_other = time_break / 4

time_watch = time_break - time_to_lunch - time_other
difference = abs(time_watch - time_epizode)
difference = ceil(difference)
if time_watch >= time_epizode:
    print(f'You have enough time to watch {name_serial} and left with {difference} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_serial}, you need {difference} more minutes.")

