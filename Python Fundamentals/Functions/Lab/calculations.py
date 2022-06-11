def calculatons(oper, first_num, sec_num):
    if oper == "multiply":
        return first_num * sec_num
    elif oper == "divide":
        return first_num // sec_num
    elif oper == "add":
        return first_num + sec_num
    elif oper == "subtract":
        return first_num - sec_num


operator = input()
num_1 = int(input())
num_2 = int(input())

print(calculatons(operator, num_1, num_2))
