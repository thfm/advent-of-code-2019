import unittest
from src import day_two


class TestIntcodeComputer(unittest.TestCase):
    def test_mul_opcode(self):
        self.assertEqual(day_two.mul([1, 2, 3, 4]), 24)
        self.assertEqual(day_two.mul([-5, -3, 15]), 225)

    def test_output(self):
        self.assertEqual(day_two.run_intcode_program([1, 0, 0, 0, 99])[0], 2)
        self.assertEqual(day_two.run_intcode_program([2, 4, 4, 5, 99, 0])[5], 9801)
