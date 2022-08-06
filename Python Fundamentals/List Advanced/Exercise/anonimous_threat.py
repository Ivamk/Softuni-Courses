
virus_string = input().split()
while True:
    command = input()
    if command == "3:1":
        print(" ".join(virus_string))
        break
    command = command.split()
    action = command[0]
    if action == "merge":
        index_start = int(command[1])
        index_end = int(command[2])
        if index_start < 0:
            index_start = 0
        if index_end >= len(virus_string):
            index_end = len(virus_string) - 1
        for seq in range(index_start, index_end):
            virus_string[index_start] = virus_string[index_start] + virus_string[index_start+1]
            virus_string.pop(index_start+1)
    if action == "divide":
        index = int(command[1])
        partions_divided = int(command[2])
        element = virus_string[index]
        element_new = []
        if len(element) % partions_divided == 0:
            divider = int(len(element) / partions_divided)

            for i in range(0, len(element), divider):
                element_new.append(element[i:(i + divider)])

            virus_string[index:index+1] = element_new
        else:
            divider = len(element) // partions_divided
            for i in range(0, len(element)-divider-1, divider):
                element_new.append(element[i:(i + divider)])
            element_new.append(element[len(element)-divider-1:])
            virus_string[index:index + 1] = element_new


