"""
Functions to test conversion

Author: Matt Reid
"""

# Converts given liquid distance into it mL amount
def distance_to_volume(distance):
    # The distance to volume conversion was calculated using a trendline in excel
    volume = (52.467 * distance) + 33.503

    return volume

# Function to get the closest cup volume (every 80mL) to the given volume
def closest_volume(volume, value=80):

    # Check if the volume is negative or greater than the max (640mL)
    if volume < 0 or volume > 640:
        return -1
    
    # Less than 80mL is considered empty
    if volume < 80:
        return 0
    
    # Round to closest multiple of 80
    return (value * round(volume/value))
