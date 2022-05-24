hour = int(input())
day_of_the_week = input()

if 18 < hour < 24 or 1 < hour < 10 or day_of_the_week == 'Sunday':
    print('closed')
else:
    print('open')
