import sys

def is_valid(index, nums):
    if 0 <= index < len(nums):
        return True
    else:
        return False


numbers = [int(el) for el in input().split()]
command = input()
while not command == "end":
    command = str(command).split(" ")
    if command[0] == "exchange":
        index = int(command[1])
        if is_valid(index, numbers):
            sub_list_1 = numbers[:index+1]
            sub_list_2 = numbers[index+1:]
            numbers = sub_list_2 + sub_list_1
        else:
            print("Invalid index")
    if command[0] == "max":
        max_num = -sys.maxsize
        max_number_index = -1
        if command[1] == "even":
            for i in range(len(numbers)):
                nums = numbers[i]
                if nums % 2 == 0 and nums >= max_num:
                    max_num = nums
                    max_number_index = i
        elif command[1] == "odd":
            for i in range(len(numbers)):
                nums = numbers[i]
                if not nums % 2 == 0 and nums >= max_num:
                    max_num = nums
                    max_number_index = i
        if not max_num == - sys.maxsize:
            print(max_number_index)
        else:
            print(f"No matches")
    if command[0] == "min":
        min_num = sys.maxsize
        min_number_index = -1
        if command[1] == "even":
            for i in range(len(numbers)):
                nums = numbers[i]
                if nums % 2 == 0 and nums <= min_num:
                    min_num = nums
                    min_number_index = i
        elif command[1] == "odd":
            for i in range(len(numbers)):
                nums = numbers[i]
                if not nums % 2 == 0 and nums <= min_num:
                    min_num = nums
        if not min_num == sys.maxsize:
            print(numbers.index(min_num))
        else:
            print("No matches")
    if command[0] == "first":
        count = int(command[1])
        if count > len(numbers):
            print("Invalid count")
            continue
        new_list = []
        if command[2] == "even":
            for nums in numbers:
                if nums % 2 == 0 and count > 0:
                    new_list.append(nums)
                    count -= 1
        elif command[2] == 'odd':
            for nums in numbers:
                if nums % 2 != 0 and count > 0:
                    new_list.append(nums)
                    count -= 1
        if len(new_list) == 0:
            print("[]")
        else:
            print(new_list)

    if command[0] == "last":
        count = int(command[1])
        if count > len(numbers):
            print("Invalid count")
            continue
        new_list = []
        numbers = numbers[::-1]
        if command[2] == "even":
            for nums in numbers:
                if nums % 2 == 0 and count > 0:
                    new_list.append(nums)
                    count -= 1
        elif command[2] == 'odd':
            for nums in numbers:
                if nums % 2 != 0 and count > 0:
                    new_list.append(nums)
                    count -= 1
        numbers = numbers[::-1]
        if len(new_list) == 0:
            print("[]")
        else:
            print(new_list)
    command = input()
print(numbers)