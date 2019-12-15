import unittest
from src.day_three import *


class TestCoordinateCalculation(unittest.TestCase):
    def test_delta_distances_calculation(self):
        self.assertEqual(calculate_delta_distances("R30"), (30, 0))
        self.assertEqual(calculate_delta_distances("L10"), (-10, 0))
        self.assertEqual(calculate_delta_distances("U0"), (0, 0))
        self.assertEqual(calculate_delta_distances("D23"), (0, -23))


    def test_nums_in_between_calculation(self):
        self.assertEqual(calculate_nums_between(5, 10), [6, 7, 8, 9])
        self.assertEqual(calculate_nums_between(-3, -6), [-4, -5])
        self.assertEqual(calculate_nums_between(8, 8), [])


    def test_joining_coordinate_calculation(self):
        self.assertEqual(calculate_joining_coords((0, 0), (5, 0)),
                         [(1, 0), (2, 0), (3, 0), (4, 0)])
        self.assertEqual(calculate_joining_coords((0, -3), (0, -6)),
                         [(0, -4), (0, -5)])


class TestIntersectionCalculation(unittest.TestCase):
    def test_intersection_calculation(self):
        self.assertEqual(
            get_intersections(Wire(["R8", "U5", "L5", "D3"]), Wire(["U7", "R6", "D4", "L4"])),
            [(3, 3), (6, 5)]
        )
