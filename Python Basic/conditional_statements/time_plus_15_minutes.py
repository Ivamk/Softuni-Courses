hours = int(input())
minutes = int(input())

minutes += 15
# hours = hours + minutes // 60
hours += minutes // 60

# minutes = minutes % 60
minutes %= 60

if hours > 23:
    hours = 0

# print(f'{hours}:{minutes:02d})  тогава си спестяваме писането на if и else по-долу
if minutes < 10:
    print(f'{hours}:0{minutes}')

else:
    print(f'{hours}:{minutes}')

