import unittest
from src.intcode import intcode


class TestIntcodeComputer(unittest.TestCase):
    def test_instruction_decoding(self):
        self.assertEqual(intcode.decode_instruction("5"),
                         ("05", ["0", "0", "0"]))
        self.assertEqual(intcode.decode_instruction("1104"),
                         ("04", ["1", "1", "0"]))
        self.assertEqual(intcode.decode_instruction("10001"),
                         ("01", ["0", "0", "1"]))
