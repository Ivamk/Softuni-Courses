number = int(input())
for seq in range(1, number + 1):
    number_as_string = str(seq)
    result = 0
    for i in number_as_string:
        result += int(i)
    if result == 5 or result == 7 or result == 11:
        print(f'{seq} -> True')
    else:
        print(f'{seq} -> False')
