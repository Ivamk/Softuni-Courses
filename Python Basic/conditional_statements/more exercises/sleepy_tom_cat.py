number_holidays = int(input())

standard_to_play = 30000
working_days = 365 - number_holidays
time_to_play = working_days * 63 + number_holidays * 127

difference = abs(time_to_play - standard_to_play)
hours = difference // 60
minutes = difference % 60

if time_to_play > standard_to_play:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
