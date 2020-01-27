def read_input_paths(filename):
    paths = []
    for line in open(filename).readlines():
        paths.append(line.strip().split(","))
    return paths


# Calculate the change in location on both the horizontal and vertical
# axes caused by a step instruction (e.g. R29)
def calculate_delta_distances(step):
    direction = step[0]
    magnitude = int(step[1:])
    dx = dy = 0

    if direction == "R":
        dx = magnitude
    elif direction == "L":
        dx = -magnitude
    elif direction == "U":
        dy = magnitude
    elif direction == "D":
        dy = -magnitude

    return (dx, dy)


# Calculate the integer values between two points
def calculate_nums_between(x0, x1):
    direction = -1 if x0 > x1 else 1
    return list(range(x0 + direction, x1, direction))


# Calculate the 2D coordinates between two points
def calculate_joining_coords(p0, p1):
    joining_coords = []
    # If the x-value is not the same...
    if p0[0] != p1[0]:
        for x in calculate_nums_between(p0[0], p1[0]):
            joining_coords.append((x, p0[1]))
    else:
        for y in calculate_nums_between(p0[1], p1[1]):
            joining_coords.append((p0[0], y))
    return joining_coords


BASE_POINT = (0, 0)


# Calculate all line coordinates from a sequence of steps
# i.e a 'path'
def calculate_line_coordinates(path):
    # The 2D coordinates at the ends of each line
    points = [BASE_POINT]
    # The 2D coordinates in between each point
    segments = []
    for i, step in enumerate(path):
        deltas = calculate_delta_distances(step)
        current_point = points[i]
        next_point = (current_point[0] + deltas[0], current_point[1] + deltas[1])
        segments.append(calculate_joining_coords(current_point, next_point))
        points.append(next_point)

    # Joining points and segments in order of step sequence
    all_coords = [BASE_POINT]
    for i, point in enumerate(points[1:]):
        for coord in segments[i]:
            all_coords.append(coord)
        all_coords.append(point)
    return all_coords


class Wire:
    def __init__(self, path):
        self.coords = calculate_line_coordinates(path)


# Calculates the points that are shared between two wires
def get_intersections(wire0, wire1):
    intersects = list(set(wire0.coords).intersection(set(wire1.coords)))
    intersects.remove(BASE_POINT)
    return intersects


# Calculates the amount of steps taken by both wires to reach a
# certain intersection
def get_combined_steps(wire0, wire1, intersection):
    return wire0.coords.index(intersection) + wire1.coords.index(intersection)


# Calculates the intersection between two wires that has the shortest
# amount of combined steps to reach
def get_closest_step_intersection(wire0, wire1):
    intersections = get_intersections(wire0, wire1)
    # Initialise the closest step count as that of the first intersection
    closest_steps = get_combined_steps(wire0, wire1, intersections[0])
    for intersect in intersections[1:]:
        steps = get_combined_steps(wire0, wire1, intersect)
        if steps < closest_steps:
            closest_steps = steps
    return closest_steps


WIRES = []
for path in read_input_paths("res/day_three_inputs.txt"):
    WIRES.append(Wire(path))
print(get_closest_step_intersection(WIRES[0], WIRES[1]))
