number = int(input())
for seq in range(1, number + 1):
    result = 0
    digits = seq
    while digits > 0:
        result += digits % 10
        digits = digits // 10
    if result == 5 or result == 7 or result == 11:
        print(f'{seq} -> True')
    else:
        print(f'{seq} -> False')
