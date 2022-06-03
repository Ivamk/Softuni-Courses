gift_list = input().split()
command = input()
command_list = command.split(' ')
while command != 'No Money':
    command_list = command.split(' ')
    if 'OutOfStock' in command_list:
        for index in range(len(gift_list)):
            if gift_list[index] == command_list[1]:
                gift_list[index] = "None"
    if 'Required' in command_list:
        if 0 <= int(command_list[2]) <= len(gift_list) - 1:
            gift_list[int(command_list[2])] = command_list[1]
    if 'JustInCase' in command_list:
        gift_list[len(gift_list) - 1] = command_list[1]
    command = input()
for _ in range(len(gift_list)):
    if "None" in gift_list:
        gift_list.remove("None")
print(" ".join(gift_list))
