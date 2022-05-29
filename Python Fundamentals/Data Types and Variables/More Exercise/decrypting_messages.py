key = int(input())
number_lines = int(input())
result = 0
for i in range(number_lines):
    current_letter = input()
    result = ord(current_letter) + key
    print(f"{chr(result)}", end='')
    result = 0

