def is_exist(lst, lesson_title):
    if lesson_title in lst:
        return True
    return False


def add_lesson(schedule, lesson):
    if not is_exist(schedule, lesson):
        schedule.append(lesson)
        return schedule
    return schedule


def insert_lesson(schedule, lesson, index):
    if not is_exist(schedule, lesson):
        schedule.insert(index, lesson)
        return schedule
    return schedule


def remove_lesson(schedule, lesson):
    if is_exist(schedule, lesson):
        schedule.remove(lesson)
        if f"{lesson}-Exercise" in schedule:
            schedule.remove(f"{lesson}-Exercise")
        return schedule
    return schedule


def swap_lesson(schedule, lesson_one, lesson_two):
    index_one = schedule.index(lesson_one)
    index_two = schedule.index(lesson_two)
    if is_exist(schedule, lesson_one) and is_exist(schedule, lesson_two):
        schedule[index_one], schedule[index_two] = schedule\
         [index_two], schedule[index_one]
        if f"{lesson_one}-Exercise" in schedule:
            schedule.remove(f"{lesson_one}-Exercise")
            schedule.insert(index_two + 1, f"{lesson_one}-Exercise")
        if f"{lesson_two}-Exercise" in schedule:
            schedule.remove(f"{lesson_two}-Exercise")
            schedule.insert(index_one + 1, f"{lesson_two}-Exercise")
        return schedule
    return schedule


def exercise_lesson(schedule, lesson):
    if not is_exist(schedule, lesson):
        schedule.append(lesson)
        schedule.append(f"{lesson}-Exercise")
    else:
        if f"{lesson}-Exercise" not in schedule:
            schedule.insert(schedule.index(lesson)+1, f"{lesson}-Exercise")
    return schedule


initial_schedule = input().split(", ")
command = input()
while not command == "course start":
    command = command.split(":")
    action = command[0]
    if action == "Add":
        initial_schedule = add_lesson(initial_schedule, command[1])
    elif action == "Insert":
        initial_schedule = insert_lesson(initial_schedule, command[1], int(command[2]))
    elif action == "Remove":
        initial_schedule = remove_lesson(initial_schedule, command[1])
    elif action == "Swap":
        initial_schedule = swap_lesson(initial_schedule, command[1], command[2])
    elif action == "Exercise":
        initial_schedule = exercise_lesson(initial_schedule, command[1])
    command = input()

print('\n'.join(f"{initial_schedule.index(el)+1}.{el}" for el in initial_schedule))

