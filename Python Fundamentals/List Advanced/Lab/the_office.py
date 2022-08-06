employees_happiness = [int(el) for el in input().split()]
factor = int(input())

multiplied_happiness = [el * factor for el in employees_happiness]

average = sum(multiplied_happiness) / len(multiplied_happiness)

happy_employees = [el for el in multiplied_happiness if el >= average]
sad_employees = [el for el in multiplied_happiness if el < average]

if len(happy_employees) >= len(multiplied_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness)}. Employees are not happy!")
