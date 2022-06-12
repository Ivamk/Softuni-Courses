def data_type(type, number):
    result = 0
    if type == "int":
        return int(number) * 2
    elif type == "real":
        result = float(number) * 1.5
        return (f"{result:.2f}")
    elif type == "string":
        return (f"${number}$")

type = input()
number_or_string = input()
print(data_type(type, number_or_string))
