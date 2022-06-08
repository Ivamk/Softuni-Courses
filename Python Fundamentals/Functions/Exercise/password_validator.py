def len_is_ok(passw):
    if 6 <= len(passw) <= 10:
        return True
    return False


def all_numalpha(passw):
    if passw.isalnum():
        return True
    return False

def num_digits (passw):
    count_digit = 0
    for el in passw:
        if el.isdigit() == True:
            count_digit += 1
    if count_digit >= 2:
        return True
    else:
        return False

def valid_password(passw):
    is_valid = True

    if not len_is_ok(passw):
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not all_numalpha(passw):
        print("Password must consist only of letters and digits")
        is_valid = False
    if not num_digits(passw):
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")

validator = input()
valid_password(validator)

