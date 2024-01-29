"""
Simulates the liquid level system of the Mocktender.
Sends liquid levels based on a prespecified amount and
subtract the total when dispensing a liquid.

Author: Matt Reid 101140593

"""
# Imports
from UltrasonicSimulatedSensor import UltrasonicSimulatedSensor
import time
import pyrebase
import os
import json

# Constants and configs
DB_USERNAME = "SystemSimulator"
LIQUID1_DATASET = "LiquidLevel1"
LIQUID2_DATASET = "LiquidLevel2"
LIQUID3_DATASET = "LiquidLevel3" 
RECIPE_ID = "cartilage"
RECIPE = "recipe"
DISPENSING = "dispensing"
CONFIG = json.loads(os.environ['MOCKTENDERDBCONFIG'])

if __name__ == '__main__':

    # init simulated sensors with (volume,max)
    sensor1 = UltrasonicSimulatedSensor(460,640)
    sensor2 = UltrasonicSimulatedSensor(140,640)
    sensor3 = UltrasonicSimulatedSensor(600,640)

    # init firebase database
    firebase = pyrebase.initialize_app(CONFIG)
    db = firebase.database()

    # Periodic timing loop
    while True:
        # get current time
        dtime = time.strftime("%Y-%m-%d %H:%M:%S")

        # get current volumes
        volume_1 = sensor1.get_volume()
        volume_2 = sensor2.get_volume()
        volume_3 = sensor3.get_volume()
        
        # Upload liquid level to DB
        db.child(DB_USERNAME).child(LIQUID1_DATASET).child(dtime).set(volume_1)
        db.child(DB_USERNAME).child(LIQUID2_DATASET).child(dtime).set(volume_2)
        db.child(DB_USERNAME).child(LIQUID3_DATASET).child(dtime).set(volume_3)
        
        # Get the recipe data (to check if dispensing)
        data = dict(db.child(RECIPE_ID).child(RECIPE).get().val())

        # If liquid is being dispensed subtract the volumes
        if data.get(DISPENSING):
            sensor1.decrease_volume(db.child(RECIPE_ID).child(RECIPE).get(LIQUID1_DATASET).val())
            sensor2.decrease_volume(db.child(RECIPE_ID).child(RECIPE).get(LIQUID1_DATASET).val())
            sensor3.decrease_volume(db.child(RECIPE_ID).child(RECIPE).get(LIQUID1_DATASET).val())

        time.sleep(10)
