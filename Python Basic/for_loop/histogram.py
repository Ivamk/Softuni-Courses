number = int(input())
numbers_p1 = 0
numbers_p2 = 0
numbers_p3 = 0
numbers_p4 = 0
numbers_p5 = 0
sum_all_numbers = 0
for sequence in range(number):
    current_number = int(input())
    if current_number < 200:
        numbers_p1 += 1
    elif current_number < 400:
        numbers_p2 += 1
    elif current_number < 600:
        numbers_p3 += 1
    elif current_number < 800:
        numbers_p4 += 1
    else:
        numbers_p5 += 1
p1 = numbers_p1 / number * 100
p2 = numbers_p2 / number * 100
p3 = numbers_p3 / number * 100
p4 = numbers_p4 / number * 100
p5 = numbers_p5 / number * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')




