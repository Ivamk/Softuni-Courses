initial_list = input().split(' ')
killed_position = int(input())
new_list = []
counter = 0
index = 0
new_list_int = []
while len(initial_list) > 0:
    counter += 1
    if counter % killed_position == 0:
        new_list.append(initial_list.pop(index))
    else:
        index += 1
    if index >= len(initial_list):
        index = 0
for el in new_list:
    new_list_int.append(int(el))
print(str(new_list_int).replace(' ', ''))
