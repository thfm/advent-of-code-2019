import unittest
from src.day_eight import SpaceImage, get_layers, get_pixel_colour


class TestImageDecoding(unittest.TestCase):
    def test_layer_calculation(self):
        self.assertEqual(get_layers(SpaceImage(3, 2, "123456789012")),
                         ["123456", "789012"])
        self.assertEqual(get_layers(SpaceImage(1, 5, "1357902468")),
                         ["13579", "02468"])


    def test_pixel_colour_calculation(self):
        self.assertEqual(get_pixel_colour(
            ["0222", "1122", "2212", "0000"], 3), "0")
        self.assertEqual(get_pixel_colour(
            ["2210", "1100", "0112", "0011"], 1), "1")
