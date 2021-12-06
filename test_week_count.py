import unittest
from week_count import week_count
from datetime import date


# The Unittest module
class TestCircleArea(unittest.TestCase):
    # correct calculalion check
    def test_area(self):
        self.assertAlmostEqual(week_count(date(2021, 1, 6)), 106)
        self.assertAlmostEqual(week_count(date(2019, 1, 5)), 1)
        self.assertAlmostEqual(week_count(date(2019, 1, 6)), 2)

    # correct date range check
    def test_values(self):
        self.assertRaises(ValueError, week_count, date(2001, 1, 6))

    # correct type check
    def test_types(self):
        self.assertRaises(TypeError, week_count, "text")
        self.assertRaises(TypeError, week_count, 1)
