notes = [0] * 10

command = input()

while not command == "End":
    importance, note = command.split("-")
    current_index = int(importance) - 1
    notes[current_index] = note
    command = input()

print ([el for el in notes if not el == 0])
