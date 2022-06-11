numbers_str = input().split()
numbers = []
for element in numbers_str:
    numbers.append(abs(float(element)))
print(numbers)
