number = int(input())

for seq in range(number):
    current_string = input()
    if "," in current_string or "." in current_string or "_" in current_string:
        print(f"{current_string} is not pure!")

        break
    else:
        print(f"{current_string} is pure.")



# number = int(input())
# string_pure = True
# for seq in range(number):
#     current_string = input()
#     for s in current_string:
#         if s == "," or s == "." or s == "_":
#             print(f"{current_string} is not pure!")
#             string_pure = False
#             break
#     if string_pure:
#         print(f"{current_string} is pure.")