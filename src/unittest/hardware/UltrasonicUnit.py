"""
Unit tests for ultrasonic hardware
Measures various distance thresholds and
gets the standard deviation.

Author: Matt Reid
"""

from gpiozero import DistanceSensor
import time
import numpy as np
from UltrasonicSensor import calculate_distance

CUP_SIZE = 16.3 # Cup size in cm

def calculate_distance_10(ultrasonic):

    distances = []

    for i in range (1, 10):
        dist = calculate_distance(ultrasonic)
        print("Distance %d: %.5fcm" % (i, dist))
        print("Water Level %d: %.5fcm\n" % (i, (CUP_SIZE - dist)))

        distances.append(dist)
        time.sleep(1)
    
    return distances

def distance_list_processing(dist_list, expected):
    print("Average Distance: %.5fcm"  % np.mean(dist_list))
    print("Average Water Level: %.5fcm"  % (CUP_SIZE - np.mean(dist_list)))
    print("Standard Deviation: %.5fcm" % np.std(dist_list))

    if (abs((CUP_SIZE - np.mean(dist_list)) - expected) < 0.5):
        print("\nTEST PASS: Within 5mm of expected (" + str(expected) + ")")
    else:
        print("\nTEST FAIL: Not within 5mm of expected (" + str(expected) + ")")

if __name__ == '__main__':

    ultrasonic = DistanceSensor(echo=21, trigger=20)

    print("Testing Ultrasonic Sensor with cup size: " + str(CUP_SIZE))

    input("\n\nTest 1: Ensure that the cup is empty and press enter\n")
    distance_list_processing(calculate_distance_10(ultrasonic), 0)
        
    input("\n\nTest 2: Ensure that the cup is filled to 2cm and press enter\n")
    distance_list_processing(calculate_distance_10(ultrasonic), 2)

    input("\n\nTest 3: Ensure that the cup is filled to 4cm and press enter\n")
    distance_list_processing(calculate_distance_10(ultrasonic), 4)

    input("\n\nTest 4: Ensure that the cup is filled to 6cm and press enter\n")
    distance_list_processing(calculate_distance_10(ultrasonic), 6)

    input("\n\nTest 4: Ensure that the cup is filled to 8cm and press enter\n")
    distance_list_processing(calculate_distance_10(ultrasonic), 8)

    input("\n\nTest 5: Ensure that the cup is filled to 10cm and press enter\n")
    distance_list_processing(calculate_distance_10(ultrasonic), 10)
    
