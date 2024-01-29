# Imports
from gpiozero import DistanceSensor

# Function to get the distance from the sensor
def calculate_distance(ultrasonic: DistanceSensor):

    return ultrasonic.distance * 100 + 1.3 # Return the measure distance in cm
    
