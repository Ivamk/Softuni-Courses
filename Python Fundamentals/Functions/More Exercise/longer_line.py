import math

def get_hipotenuse(num1, num2):
    x = math.pow(num1, 2)
    y = math.pow(num2, 2)
    return math.sqrt(x + y)


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))
x3 = math.floor(float(input()))
y3 = math.floor(float(input()))
x4 = math.floor(float(input()))
y4 = math.floor(float(input()))
z1 = get_hipotenuse(x1, y1)
z2 = get_hipotenuse(x2, y2)
z3 = get_hipotenuse(x3, y3)
z4 = get_hipotenuse(x4, y4)

if z1 + z2 < z3 + z4:
    if z3 < z4:
        print(f"({x3}, {y3})({x4}, {y4})")
    else:
        print(f"({x4}, {y4})({x3}, {y3})")
else:
    if z1 < z2:
        print(f"({x1}, {y1})({x2}, {y2})")
    else:
        print(f"({x2}, {y2})({x1}, {y1})")
