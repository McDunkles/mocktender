"""
Ultrasonic sensor object used to interact with the ultrasonic sensor hardware
Gives the distance in cm when requested

Author: Matt Reid
"""
from gpiozero import DistanceSensor
import time

class UltrasonicSensor:
    def __init__(self, echo_pin, trigger_pin):
        """
        Function to initialize an ultrasonic sesnor for the 
        Mocktender. Takes the echo and trigger pins
        """
        self._sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin)

    def get_distance(self):
        """
        Function to get the distance from the ultrasonic
        sensor.
        """

        return self._sensor.distance * 100 + 1.5
        
    
