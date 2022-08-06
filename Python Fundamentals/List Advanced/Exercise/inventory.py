collected_items = input(). split(", ")
command = input().split(" - ")
while not command[0] == "Craft!":
    if command[0] == "Collect":
        if command [1] not in collected_items:
            collected_items.append(command[1])
    elif command[0] == "Drop":
        if command [1] in collected_items:
            collected_items.remove(command[1])
    elif command[0] == "Combine Items":
        new_items = command[1].split(":")
        if new_items[0] in collected_items:
            pos = collected_items.index(new_items[0])
            collected_items.insert(pos+1, new_items[1])
    elif command[0] == "Renew":
        if command[1] in collected_items:
            collected_items.append(collected_items.pop(collected_items.index(command[1])))
    command = input().split(" - ")

print(*collected_items, sep=", ")
