# Формулата за лице на трапец е (b1 + b2) * h / 2.
# Отговорът трябва да е форматиран до втората цифра след десетичния знак.

side_a = float(input())
side_b = float(input())
height = float(input())

square = (side_a + side_b) * height / 2

print(f'{square:.2f}')
