text = input()

value = 0
for ch in text:
    if ch == 'a':
        value += 1
    if ch == 'e':
        value += 2
    if ch == 'i':
        value += 3
    if ch == 'o':
        value += 4
    if ch == 'u':
        value += 5
print(value)

