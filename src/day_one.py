def read_input():
    modules = []
    with open("res/day_one_inputs.txt") as f:
        for line in f:
            modules.append(int(line))
    return modules


def get_fuel_requirement(mass):
    return int(mass / 3) - 2


def get_module_fuel_requirement(module):
    total_fuel = 0
    required_fuel = get_fuel_requirement(module)
    while required_fuel > 0:
        total_fuel = total_fuel + required_fuel
        required_fuel = get_fuel_requirement(required_fuel)
    return total_fuel


total = 0
for mass in read_input():
    total = total + get_module_fuel_requirement(mass)
print(total)
