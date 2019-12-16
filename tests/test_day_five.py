import unittest
from src import day_five


class TestIntcodeComputer(unittest.TestCase):
    def test_instruction_decoding(self):
        self.assertEqual(day_five.decode_instruction("5"),
                         ("05", ["0", "0", "0"]))
        self.assertEqual(day_five.decode_instruction("1104"),
                         ("04", ["1", "1", "0"]))
        self.assertEqual(day_five.decode_instruction("10001"),
                         ("01", ["0", "0", "1"]))
