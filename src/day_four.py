import itertools

INPUTS = range(273025, 767253 + 1)


def get_digits(num):
    return list(map(int, str(num)))


def has_same_adjacent_pair(num):
    groups = [list(group) for _, group in itertools.groupby(str(num))]
    for group in groups:
        if len(group) == 2:
            return True
    return False


def never_decreases(num):
    digits = get_digits(num)
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True


count = 0
for i in INPUTS:
    if has_same_adjacent_pair(i) and never_decreases(i):
        count += 1
print(count)
