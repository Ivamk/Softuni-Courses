initial_course = input().split(", ")
command = input()
while not command == "course start":
    command = command.split(":")
    if command[0] == "Add":
        if command[1] not in initial_course:
            initial_course.append(command[1])
    elif command[0] == "Insert":
        if command[1] not in initial_course:
            initial_course.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if command[1] in initial_course:
            initial_course.remove(command[1])
            if f"{command[1]}-Exercise" in initial_course:
                initial_course.remove(f"{command[1]}-Exercise")
    elif command[0] == "Swap":
        if command[1] in initial_course and command[2] in initial_course:
            index_one = initial_course.index(command[1])
            index_two = initial_course.index(command[2])
            if f"{command[1]}-Exercise" in initial_course:
                initial_course[index_one], initial_course[index_two] = initial_course[index_two], initial_course[
                    index_one]
                initial_course.remove(f"{command[1]}-Exercise")
                initial_course.insert(index_two + 1, f"{command[1]}-Exercise")
            elif f"{command[2]}-Exercise" in initial_course:
                initial_course[index_one], initial_course[index_two] = initial_course[index_two], initial_course[
                    index_one]
                initial_course.remove(f"{command[2]}-Exercise")
                initial_course.insert(index_one + 1, f"{command[2]}-Exercise")
            elif f"{command[1]}-Exercise" in initial_course and "{command[2]}-Exercise" in initial_course:
                initial_course[index_one], initial_course[index_two] = initial_course[index_two], initial_course[
                    index_one]
                initial_course.remove(f"{command[1]}-Exercise")
                initial_course.insert(index_two + 1, f"{command[1]}-Exercise")
                initial_course.remove(f"{command[2]}-Exercise")
                initial_course.insert(index_one + 1, f"{command[2]}-Exercise")
            else:
                initial_course[index_one], initial_course[index_two] = initial_course[index_two], initial_course[
                    index_one]
    elif command[0] == "Exercise":
        if command[1] not in initial_course:
            initial_course.append(f"{command[1]}")
            initial_course.append(f"{command[1]}-Exercise")
        else:
            current_lesson_index = initial_course.index(command[1])
            initial_course.insert(current_lesson_index + 1, f"{command[1]}-Exercise")
    command = input()
for seq in range(1, len(initial_course) + 1):
    print(f'{seq}.{initial_course[seq-1]}')

