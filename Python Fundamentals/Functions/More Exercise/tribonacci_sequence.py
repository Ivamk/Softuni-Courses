def valid_index(index):
    is_valid = True
    if 0 <= index - 3:
        return is_valid
    else:
        is_valid = False
        return is_valid


number = int(input())
list = [1]
sum = 1
index = 1
while len(list) < number:
    if valid_index(index):
        sum = list[index - 1] + list[index - 2] + list[index - 3]
        list.append(sum)
    else:
        if index - 2 < 0:
            sum = list[index - 1]
            list.append(sum)
        elif index - 3 < 0:
            sum = list[index - 1] + list[index - 2]
            list.append(sum)
    index += 1

print(*list)
