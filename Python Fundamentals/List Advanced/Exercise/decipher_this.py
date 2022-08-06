text = input().split()
final_decipher = []
final = []
for el in text:
    number = ""
    new_text = []
    new_text_edno = []
    final_text = []
    for s in el:
        if s.isdigit():
            number += s
        else:
            new_text_edno.append(s)
    new_text.append(chr(int(number)))
    final_text = new_text + new_text_edno
    final_decipher.append("".join(final_text))

for word in final_decipher:
    letter = list(word)
    letter[1], letter[-1] = letter[-1], letter[1]
    final.append(''.join(letter))
print(*final)


# def int_to_chr(word):
#     string = list(word)
#     num_as_str = list()
#
#     while string[0].isdigit():
#         num_as_str.append(string[0])
#         string.pop(0)
#
#     num = int(''.join(num_as_str))
#     string.insert(0, chr(num))
#     return ''.join(string)
#
#
# def switch_letters(word):
#     letters = list(word)
#     letters[1], letters[-1] = letters[-1], letters[1]
#     return ''.join(letters)
#
#
# print(' '.join([switch_letters(int_to_chr(word)) for word in input().split()]))