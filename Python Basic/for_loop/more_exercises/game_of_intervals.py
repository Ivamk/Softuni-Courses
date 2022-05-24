number_moves = int(input())
result = 0
# p0 = 0
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
p0 = p1 = p2 = p3 = p4 = p5 = 0
for sequence in range(number_moves):
    number_separate = int(input())
    if 0 <= number_separate <= 9:
        p0 += 1
        result += number_separate * 0.2
    elif 10 <= number_separate <= 19:
        p1 += 1
        result += number_separate * 0.3
    elif 20 <= number_separate <= 29:
        p2 += 1
        result += number_separate * 0.4
    elif 30 <= number_separate <= 39:
        p3 += 1
        result += 50
    elif 40 <= number_separate <= 50:
        p4 += 1
        result += 100
    elif number_separate < 0 or number_separate > 50:
        p5 += 1
        result = result / 2

p0_percentage = p0 / number_moves * 100
p1_percentage = p1 / number_moves * 100
p2_percentage = p2 / number_moves * 100
p3_percentage = p3 / number_moves * 100
p4_percentage = p4 / number_moves * 100
p5_percentage = p5 / number_moves * 100
print(f'{result:.2f}')
print(f'From 0 to 9: {p0_percentage:.2f}%')
print(f'From 10 to 19: {p1_percentage:.2f}%')
print(f'From 20 to 29: {p2_percentage:.2f}%')
print(f'From 30 to 39: {p3_percentage:.2f}%')
print(f'From 40 to 50: {p4_percentage:.2f}%')
print(f'Invalid numbers: {p5_percentage:.2f}%')


