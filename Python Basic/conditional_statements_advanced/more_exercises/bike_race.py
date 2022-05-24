number_junior_velo = int(input())
number_senior_velo = int(input())
type_of_trace = input()

tax_junior = 0
tax_senior = 0
total_number_velo = number_junior_velo + number_senior_velo

if type_of_trace == 'trail':
    tax_junior = 5.50
    tax_senior = 7
elif type_of_trace == 'cross-country':
    tax_junior = 8
    tax_senior = 9.50
elif type_of_trace == 'downhill':
    tax_junior = 12.25
    tax_senior = 13.75
elif type_of_trace == 'road':
    tax_junior = 20
    tax_senior = 21.50

if type_of_trace == 'cross-country' and total_number_velo >=50:
    tax_junior *= 0.75
    tax_senior *= 0.75

total_income = (number_junior_velo * tax_junior + number_senior_velo * tax_senior) * 0.95

print(f'{total_income:.2f}')




