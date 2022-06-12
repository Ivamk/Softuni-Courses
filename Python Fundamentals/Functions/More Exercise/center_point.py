import math


def get_hipotenuse(num1, num2):
    x = math.pow(num1, 2)
    y = math.pow(num2, 2)
    return math.sqrt(x + y)


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))
z1 = get_hipotenuse(x1, y1)
z2 = get_hipotenuse(x2, y2)
if z1 <= z2:
    print(f"({x1}, {y1})")
else:
    print(f"({x2}, {y2})")
