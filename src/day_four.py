import itertools


def get_digits(num):
    return [int(digit) for digit in str(num)]


def has_same_adjacent_pair(num):
    # Gets the groups of adjacent numbers
    groups = [list(group) for _, group in itertools.groupby(str(num))]
    for group in groups:
        if len(group) == 2:
            return True
    return False


# Ascertains that each digit in a number is either equal to or
# greater than the digit to it's left
def never_decreases(num):
    digits = get_digits(num)
    for i in range(len(digits) - 1):
        if digits[i + 1] < digits[i]:
            return False
    return True


INPUTS = range(273025, 767253 + 1)

count = 0
for i in INPUTS:
    if has_same_adjacent_pair(i) and never_decreases(i):
        count += 1
print(count)
