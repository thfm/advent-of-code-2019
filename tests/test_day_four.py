import unittest
from src import day_four


class TestNeverDecreases(unittest.TestCase):
    def test_never_decreases(self):
        self.assertEqual(day_four.never_decreases(111111), True)
        self.assertEqual(day_four.never_decreases(223450), False)


class TestAdjacentPair(unittest.TestCase):
    def test_has_same_adjacent_pair(self):
        self.assertEqual(day_four.has_same_adjacent_pair(123789), False)
        self.assertEqual(day_four.has_same_adjacent_pair(112233), True)
        self.assertEqual(day_four.has_same_adjacent_pair(123444), False)
        self.assertEqual(day_four.has_same_adjacent_pair(111122), True)
