numbers = [int(el) for el in input().split(", ")]
count = 0
group_of_numbers = 10

while count < len(numbers):
    collected_numbers = []
    for el in numbers:
        if group_of_numbers - 10 < el <= group_of_numbers:
            collected_numbers.append(el)
            count += 1
    print(f"Group of {group_of_numbers}'s: {collected_numbers}")
    group_of_numbers += 10





