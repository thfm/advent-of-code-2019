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


def calculate_joining_coords(p0, p1):
    joining_coords = []
    if p0[0] != p1[0]:
        for x in range(p0[0] + 1, p1[0], -1 if p0[0] > p1[0] else 1):
            joining_coords.append((x, p0[1]))
    else:
        for y in range(p0[1] + 1, p1[1], -1 if p0[1] > p1[1] else 1):
            joining_coords.append((p0[0], y))
    return joining_coords


def calculate_line_coordinates(path):
    points = [(0, 0)]
    joining_coords = []
    for i, step in enumerate(path):
        dists = calculate_delta_distances(step)
        last_point = points[i]
        current_point = (last_point[0] + dists[0], last_point[1] + dists[1])
        points.append(current_point)
        for coord in calculate_joining_coords(last_point, current_point):
            joining_coords.append(coord)
    return points + joining_coords


class Wire:
    def __init__(self, coordinates):
        self.coordinates = coordinates


# Try with builtin methods? Set 'intersection()'?
def get_intersections(wire0, wire1):
    intersections = []
    for coord in wire0.coordinates:
        if coord in wire1.coordinates:
            intersections.append(coord)
    return list(set(intersections) - set([(0, 0)]))


def manhattan_distance(p0, p1):
    return abs(p1[0] - p0[0]) + abs(p1[1] - p0[1])


def get_closest_intersection(intersections):
    closest = manhattan_distance((0, 0), intersections[0])
    for intersect in intersections[1:]:
        distance = manhattan_distance((0, 0), intersect)
        if distance < closest:
            closest = distance
    return closest


wires = []
for path in read_input_paths("res/day_three_inputs.txt"):
    wires.append(Wire(calculate_line_coordinates(path)))
