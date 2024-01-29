"""
Ultrasonic sensor simulation object.
Has a volume which can be added to or taken
away from. Can be used to send volumes just like
a normal sensor

Author: Matt Reid
"""

class UltrasonicSimulatedSensor:
    def __init__(self, volume=640, max=640):
        """
        Function to initialize a simulated ultrasonic sesnor 
        for the Mocktender. Takes a starting volume (default 640)
        """
        self._volume = volume
        self._max = volume

    def get_volume(self):
        """
        Function to get the volume from the simulated
        ultrasonic sensor.
        """
        return self._volume
    
    def decrease_volume(self, amount):
        """
        Function to decrease the volume by a given amount.
        The minimum volume is zero (will not go below)
        """

        if (self._volume - amount) < 0:
            self._volume = 0
        else:
            self._volume -= amount

    def increase_volume(self, amount):
        """
        Function to increase the volume by a given amount.
        The max volume was set at init (will not go above)
        """

        if (self._volume + amount) > self._max:
            self._volume = self._max
        else:
            self._volume += amount


