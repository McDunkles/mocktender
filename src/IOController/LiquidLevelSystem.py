"""
Liquid Level System class represents a liquid level sensor system
which has 3 ultrasonic sensors that measure the water level in
the 3 liquid containers in the Mocktender machine.
Can either connect to a real ultrasonic sensor or simulated
ultrasonic sensor.

This code block defines a LiquidLevelSystem object that is
used by the I/O Controller node of the Mocktender machine.
The main purpose is to get real time distance measurements
from the machines Ultrasonic sensors and convert them to
a volume for display in the Web Interface. It is made to
be usable in either a real or simulated environment. It
will be initialized with either 3 real Ultrasonic sensors,
or 3 Ultrasonic sensor simulators and called from the
main.py periodic timing loop in order to update
the systems real time liquid level measurements.

Author: Matt Reid 101140593
Updated: March 29, 2023
"""

# Declare constants
SLOPE = 52.467  # Slope of distance to volume (linear)
INTERCEPT = 33.503  # y-intercept of distance to volume (linear)
MAX_VOL = 640  # Maximum volume of 640mL in each container
CUP_SIZE = 16.3 # Cup size in cm


# Functions for conversions
def distance_to_volume(distance):
    """
    Converts a distance measurement from the Mocktender system
    to a volume of liquid. Uses calculated formula for distance
    to volume in the Mocktender to convert distance to volume.

    Takes a float distance in cm.
    Returns a float volume in mL.
    """
    # Get the distance of the liquid from the bottom of the cup
    liquid_distance = CUP_SIZE - distance

    # Return 0 volume if negative or equal to 0
    if liquid_distance <= 0:
        return 0

    # Calculate the volume using the calculated formula
    volume = (SLOPE * liquid_distance) + INTERCEPT

    # Return the calculated volume
    return volume


def closest_volume(volume, value=80):
    """
    Rounds a given volume to the nearest multiple of the given value.
    Takes an float volume in mL and an int value to round to multiples
    of (default 80mL).

    Returns the int closest multiple in mL,
    or -1 if overfilled or negative.
    """
    # Check if the volume is greater than the max
    if volume > MAX_VOL:
        return -1

    # Less than value is considered empty
    elif volume < value:
        return 0

    # Round to closest multiple of 80
    return value * round(volume / value)


# LiquidLevelSystem Object
class LiquidLevelSystem:
    def __init__(self, sensor1, sensor2, sensor3):
        """
        Function to initialize the Liquid Level system with 3 sensors.
        The sensors can either be real or simulated sensors
        (but must have a calculate_distance function).

        Prerequisite: The sensors are previously initialized.
        """
        # Store the sensors in a list (for access by ID)
        self._sensors = [sensor1, sensor2, sensor3]

    def get_sensor(self, sensor_id):
        """
        Gets a sensor with given id.
        Takes int id.
        Returns sensor Object.
        """
        return self._sensors[sensor_id-1]

    def get_sensors(self):
        """
        Gets the list of sensors in the liquid level system.
        Returns list of sensor Objects.
        """
        return self._sensors

    def get_volume_from_sensor(self, sensor_id, value=80):
        """
        Gets a volume measurement from a specified ultrasonic sensor.
        The volume is rounded to the nearest multiple of the value
        (default 80mL).

        Takes an int id (1 to 3) to identify which sensor to get data from.
        Returns an int calculated volume.
        """
        # Get sensor to use
        sensor = self.get_sensor(sensor_id)

        # Get a distance measurement from the sensor
        sensor_distance = sensor.get_distance()

        # Convert the distance measurement to a volume
        sensor_volume = distance_to_volume(sensor_distance)
        print(sensor_volume)

        # Get the closest multiple of the value for the volume
        sensor_closest_volume = closest_volume(sensor_volume, value)

        # return the volume
        return sensor_closest_volume

    def get_all_volumes_from_sensors(self, value=80):
        """
        Gets a list of volume measurements from all three connected sensors.
        Returns a list of 3 closest volume measurements (one from each sensor).
        """
        # Get distance measurements from all 3 sensors
        # The calculate_distance() function is defined in the sensor Object
        sensor_distances = [self._sensors[0].get_distance(),
                            self._sensors[1].get_distance(),
                            self._sensors[2].get_distance()]

        # Convert the 3 distance measurements to volume measurements
        sensor_volumes = [distance_to_volume(sensor_distances[0]),
                          distance_to_volume(sensor_distances[1]),
                          distance_to_volume(sensor_distances[2])]

        # Get the nearest multiple of the 3 values
        sensor_closest_volumes = [closest_volume(sensor_volumes[0], value),
                                  closest_volume(sensor_volumes[1], value),
                                  closest_volume(sensor_volumes[2], value)]

        # return the list of closest volumes
        return sensor_closest_volumes