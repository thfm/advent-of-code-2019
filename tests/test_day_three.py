import unittest
from src import day_three


class TestCoordinateCalculation(unittest.TestCase):
    def test_delta_distances_calculation(self):
        self.assertEqual(day_three.calculate_delta_distances("R30"), (30, 0))
        self.assertEqual(day_three.calculate_delta_distances("L10"), (-10, 0))
        self.assertEqual(day_three.calculate_delta_distances("U0"), (0, 0))
        self.assertEqual(day_three.calculate_delta_distances("D23"), (0, -23))


    def test_joining_coordinate_calculation(self):
        self.assertEqual(day_three.calculate_joining_coords((0, 0), (5, 0)),
                         [(1, 0), (2, 0), (3, 0), (4, 0)])
        self.assertEqual(day_three.calculate_joining_coords((0, -3), (0, -6)),
                         [(0, -4), (0, -5)])


class TestManhattanDistance(unittest.TestCase):
    def test_manhattan_distance(self):
        self.assertEqual(day_three.manhattan_distance((3, 0), (7, -4)), 8)
        self.assertEqual(day_three.manhattan_distance((-5, -5), (-5, 110)), 115)
