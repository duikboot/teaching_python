import unittest

from speed.speed import Speed


class TestSpeed(unittest.TestCase):
    def test_zero(self):
        speed = Speed()
        self.assertEqual(speed.meter_per_second, 0.0)
        self.assertEqual(speed.kph, 0.0)
        self.assertEqual(speed.mph, 0.0)

    def test_set_kph(self):
        speed = Speed()
        speed.kph = 30
        self.assertAlmostEqual(speed.meter_per_second, 8.33, 2)
