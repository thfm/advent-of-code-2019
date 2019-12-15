def read_input_paths(filename):
    paths = []
    for line in open(filename).readlines():
        paths.append(line.strip().split(","))
    return paths


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


def calculate_nums_between(x0, x1):
    direction = -1 if x0 > x1 else 1
    return list(range(x0 + direction, x1, direction))


def calculate_joining_coords(p0, p1):
    joining_coords = []
    if p0[0] != p1[0]:
        for x in calculate_nums_between(p0[0], p1[0]):
            joining_coords.append((x, p0[1]))
    else:
        for y in calculate_nums_between(p0[1], p1[1]):
            joining_coords.append((p0[0], y))
    return joining_coords


BASE_POINT = (0, 0)


def calculate_line_coordinates(path):
    points = [BASE_POINT]
    segments = []
    for i, step in enumerate(path):
        deltas = calculate_delta_distances(step)
        last_point = points[i]
        current_point = (last_point[0] + deltas[0], last_point[1] + deltas[1])
        segments.append(calculate_joining_coords(last_point, current_point))
        points.append(current_point)

    all_coords = [BASE_POINT]
    for i, point in enumerate(points[1:]):
        for coord in segments[i]:
            all_coords.append(coord)
        all_coords.append(point)
    return all_coords


class Wire:
    def __init__(self, path):
        self.coords = calculate_line_coordinates(path)


def get_intersections(wire0, wire1):
    intersects = list(set(wire0.coords).intersection(set(wire1.coords)))
    intersects.remove(BASE_POINT)
    return intersects


def get_combined_steps(wire0, wire1, intersection):
    return wire0.coords.index(intersection) + wire1.coords.index(intersection)


def get_closest_step_intersection(wire0, wire1):
    intersections = get_intersections(wire0, wire1)
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
