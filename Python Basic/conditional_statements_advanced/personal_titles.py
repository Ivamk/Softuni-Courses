age = float(input())
sex = input()

title = ' '

if age >= 16 and sex == 'm':
    title = 'Mr.'
elif age < 16 and sex == 'm':
    title = 'Master'
elif age >= 16 and sex == 'f':
    title = 'Ms.'
elif age < 16 and sex == 'f':
    title = 'Miss'

print(title)

