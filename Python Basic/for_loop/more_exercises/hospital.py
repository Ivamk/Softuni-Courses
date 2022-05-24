number_days = int(input())
treated_patients = 0
number_doctors = 7
untreated_patients = 0
for sequence in range(1, number_days+1):
    number_patients_for_the_day = int(input())
    if sequence % 3 != 0 or (sequence % 3 == 0 and untreated_patients <= treated_patients):
        if number_patients_for_the_day <= number_doctors:
            treated_patients += number_patients_for_the_day
        else:
            treated_patients += number_doctors
            untreated_patients += number_patients_for_the_day - number_doctors
    elif sequence % 3 == 0 and untreated_patients > treated_patients:
        number_doctors += 1
        if number_patients_for_the_day <= number_doctors:
            treated_patients += number_patients_for_the_day
        else:
            treated_patients += number_doctors
            untreated_patients += (number_patients_for_the_day - number_doctors)

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
