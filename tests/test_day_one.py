import unittest
from src import day_one


class TestFuelRequirement(unittest.TestCase):
    def test_mass_fuel_requirement(self):
        self.assertEqual(day_one.get_fuel_requirement(12), 2)
        self.assertEqual(day_one.get_fuel_requirement(14), 2)
        self.assertEqual(day_one.get_fuel_requirement(1969), 654)
        self.assertEqual(day_one.get_fuel_requirement(100756), 33583)


    def test_module_fuel_requirement(self):
        self.assertEqual(day_one.get_module_fuel_requirement(14), 2)
        self.assertEqual(day_one.get_module_fuel_requirement(1969), 966)
        self.assertEqual(day_one.get_module_fuel_requirement(100756), 50346)
