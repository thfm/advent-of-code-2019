def read_input_orbits(filename):
    direct_orbits = {}
    for line in open(filename).readlines():
        parent, child = line.strip().split(")")
        direct_orbits[child] = parent
    return direct_orbits


def calculate_orbit_count(orbits):
    count = 0
    for orbit in orbits:
        parent = orbits.get(orbit)
        while parent is not None:
            count += 1
            parent = orbits.get(parent)
    return count


INPUT_ORBITS = read_input_orbits("res/day_six_inputs.txt")
print(calculate_orbit_count(INPUT_ORBITS))
