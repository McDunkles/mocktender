"""
Liquid Level Software tests.
Tests that distances are correctly
converted to volumes in the liquid
level system.

Author: Matt Reid
"""
import LiquidLevelSensor
import unittest

class TestUltrasonic(unittest.TestCase):

    # Test water level from distance in increments of 0.1cm
    def test_water_levels(self):

        # 0mL should be until a distance of 0.9cm
        distances = (x * 0.1 for x in range(0, 8))
        for distance in distances:
            with self.subTest(msg = "Testing 0mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 0, "Closest volume should be 0mL")
        
        # 80mL should be from 0.9cm to 1.6cm
        distances = (x * 0.1 for x in range(9, 16))
        for distance in distances:
            with self.subTest(msg = "Testing 80mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 80, "Closest volume should be 80mL")

        # 160mL should be from 1.7cm to 3.1cm
        distances = (x * 0.1 for x in range(17, 31))
        for distance in distances:
            with self.subTest(msg = "Testing 160mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 160, "Closest volume should be 160mL")

        # 240mL should be from 3.2cm to 4.6cm
        distances = (x * 0.1 for x in range(32, 46))
        for distance in distances:
            with self.subTest(msg = "Testing 240mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 240, "Closest volume should be 240mL")

        # 320mL should be from 4.7cm to 6.2cm
        distances = (x * 0.1 for x in range(47, 62))
        for distance in distances:
            with self.subTest(msg = "Testing 320mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 320, "Closest volume should be 320mL")

        # 400mL should be from 6.3cm to 7.7cm
        distances = (x * 0.1 for x in range(63, 77))
        for distance in distances:
            with self.subTest(msg = "Testing 400mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 400, "Closest volume should be 400mL")

        # 480mL should be from 7.8cm to 9.2cm
        distances = (x * 0.1 for x in range(78, 92))
        for distance in distances:
            with self.subTest(msg = "Testing 480mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 480, "Closest volume should be 480mL")

        # 560mL should be from 9.3cm to 10.7cm
        distances = (x * 0.1 for x in range(93, 107))
        for distance in distances:
            with self.subTest(msg = "Testing 560mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 560, "Closest volume should be 560mL")
        
        # 640mL should be from 10.8cm to 11.5cm
        distances = (x * 0.1 for x in range(108, 115))
        for distance in distances:
            with self.subTest(msg = "Testing 640mL conversions", distance=distance):
                vol = LiquidLevelSensor.distance_to_volume(distance)
                closest_vol = LiquidLevelSensor.closest_volume(vol)
                self.assertEqual(closest_vol, 640, "Closest volume should be 640mL")
    
    # Test using a negative volume
    def test_negative_water(self):
        negative_list = [-0.01 , -2, -142, -10000]
        for volume in negative_list:
            closest_vol = LiquidLevelSensor.closest_volume(volume)
            self.assertEqual(closest_vol, -1, "Negative volume should give -1 as closest volume")

    # Test using an overfilled volume (more than 640 mL)
    def test_overfill(self):
        overfill_list = [640.01 , 641, 1000, 10000]
        for volume in overfill_list:
            closest_vol = LiquidLevelSensor.closest_volume(volume)
            self.assertEqual(closest_vol, -1, "Overfill error should give -1 as closest volume")


if __name__ == '__main__':
    unittest.main()
