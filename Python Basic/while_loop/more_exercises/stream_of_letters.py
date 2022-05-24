command = input()
if_n = False
if_o = False
if_c = False
sentence = ""
while command != "End":
    num = ord(command)
    if num in range(65, 91) or num in range(97, 123):
        char = chr(num)
        if char == "n" and if_n is False:
            if_n = True
        elif char == "o" and if_o is False:
            if_o = True
        elif char == "c" and if_c is False:
            if_c = True
        else:
            sentence += char
    if if_n and if_o and if_c:
        print(sentence, end=" ")
        if_n = False
        if_o = False
        if_c = False
        sentence = ""
    command = input()
