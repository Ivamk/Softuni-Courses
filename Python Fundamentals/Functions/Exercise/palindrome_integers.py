number_list = input().split(", ")
number_forward = ""
number_backward = ""
for number in number_list:
    number_forward = number
    number_backward = number[::-1]
    if number_forward == number_backward:
        print("True")
    else:
        print("False")
#

# number_list = input().split(", ")
# resultArr = list(map(lambda x: 'True' if (x == x[::-1]) else 'False', number_list))
# print("\n".join(resultArr))