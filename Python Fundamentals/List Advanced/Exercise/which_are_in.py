first_seq = input().split(", ")
second_seq = input().split(", ")

substrings = []

for el in first_seq:
    for els in second_seq:
        if el in els and el not in substrings:
            substrings.append(el)

print(substrings)
