command = input()
powerful_word = ''
max_points = 0
current_number = 0
while command != 'End of words':
    for sequence in range(len(command)):
        current_number += ord(command[sequence])
    if command[0] in 'AaEeIiOoUuYy':
        current_number = current_number * len(command)
    else:
        current_number = current_number // len(command)
    if current_number > max_points:
        max_points = current_number
        powerful_word = command
    command = input()
    current_number = 0
print(f'The most powerful word is {powerful_word} - {max_points}')


# words = ['apple', 'orange', 'pear', 'milk', 'otter', 'snake','iguana','tiger','eagle']
# for word in words:
#     if word[0] in 'aeiou':
#         print(word)
