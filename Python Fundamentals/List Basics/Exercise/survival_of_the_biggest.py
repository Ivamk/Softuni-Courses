numbers_str = input().split()
numbers = []
count_to_remove = int(input())
final_numbers = []
for element in numbers_str:
    numbers.append(int(element))

for index in range(count_to_remove):
    numbers.remove(min(numbers))

for i in numbers:
    final_numbers.append(str(i))
print(", ".join(final_numbers))

