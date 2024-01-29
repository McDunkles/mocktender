"""
System simulator to simulate the liquid pumping system.
Instead of pumps the output is displayed on connected LEDs.

Author: Ethan Bradley
"""

from LiquidPump import LiquidPump
from pyrebase import initialize_app as initApp
from MocktenderConfig import MocktenderConfig
from pyrebase.pyrebase import Database
from collections import OrderedDict
from functools import partial
from time import sleep
from sys import argv
import asyncio

# Configuration details
FIREBASE_MOTOR_NAMES: list[str] = "l1,l2,l3".split(",")
MOCKTENDER_CONFIG = MocktenderConfig()
CONFIG_PROD = MocktenderConfig.CONFIG_PROD
CONFIG_DEV = MocktenderConfig.CONFIG_DEV

# --- Keywords used in the firebase real time database ---

# Recipe related keywords
ACK = "ack"
READY = "ready"
RECIPE = "recipe"
DISPENSING = "dispensing"

# Liquid level keywords
LIQUID1_DATASET = "LiquidLevel1"
LIQUID2_DATASET = "LiquidLevel2"
LIQUID3_DATASET = "LiquidLevel3"

# Pumping wait times
WAIT = 0.1

def validateNodeFormat(data: dict):
    '''
    Verifies that the database query response provides
    an accurate format for the data.

    data requires the following keys:
    >>> data = {"ack", "ready", "drinkSize", "drinkPercentages"}

    the drinkPercentages key needs to have the following structure
    >>> drinkPercentages = {"l1", "l2", "l3"}
    '''
    recipeKeys = "ack,ready,drinkSize,drinkPercentages".split(",")
    hasAllRecipeKeys = all(x in data for x in recipeKeys)
    
    percentKeys = FIREBASE_MOTOR_NAMES.copy()
    percentages = data.get("drinkPercentages")

    if percentages is None:
        return False
    
    hasAllPercentKeys = all(x in percentages for x in percentKeys)
    
    return hasAllPercentKeys and hasAllRecipeKeys

def validateTimingFormat(pumpTiming: dict[str, float]) -> bool:
    '''
    Verify that the recipe pump timings are correct
    pumpTiming requires the following keys:
    >>> pumpTiming = {"l1", "l2", "l3"}
    '''
    return all(mName in pumpTiming.keys() for mName in FIREBASE_MOTOR_NAMES)


def acknowledgeRecipe(node: Database):
    ''' 
    Sets the "ack" flag in the firebase recipe
    to true
    '''
    node.child(RECIPE).child(ACK).set(True)

def lockDispenser(node: Database):
    ''' 
    Sets the "dispensing" flag in the firebase mocktender
    to true
    '''
    node.child(DISPENSING).set(True)

def unlockDispensing(node: Database):
    ''' 
    Sets the "dispensing" flag in the firebase mocktender
    to false
    '''
    node.child(DISPENSING).set(False)

def getLiquidLevels(node: Database):
    '''
    Gets the most recent liquid levels of each liquid as provided
    by the Firebase real time database
    '''
    ID = MOCKTENDER_CONFIG.getId()
    level1 = node.child(ID).child(LIQUID1_DATASET).order_by_key().limit_to_last(1).get().val()
    level2 = node.child(ID).child(LIQUID2_DATASET).order_by_key().limit_to_last(1).get().val()
    level3 = node.child(ID).child(LIQUID3_DATASET).order_by_key().limit_to_last(1).get().val()
    return [list(level.values()).pop() for level in (level1, level2, level3)]

def drinkMaker(message: dict, motors: dict[str, LiquidPump], database: Database):
    '''
    Streams the recipe node of the Mocktender Firebase Real-time database.

    If the machine has not been locked and / or there is a new recipe,
    this function will actuate the liquid pumps, initially for a calculated
    amount of time based on the total liquid volume and the percentage
    of a liquid.

    In the case of a simulated system, there is no need to make calls
    for a feedback loop, and we can assume the simulated pump behaviour to
    be ideal.
    '''
    ID = MOCKTENDER_CONFIG.getId()
    data = dict(database.child(ID).child(RECIPE).get().val())

    # check for new recipe or if machine is locked
    if data.get(ACK) or not data.get(READY):
        return

    # check that data format is correct
    if not validateNodeFormat(dict(data)):
        return
    
    pumpTiming: dict[str, float] = LiquidPump.validateRecipe(data)

    # check that timing format is correct
    if not validateTimingFormat(pumpTiming):
        return
    
    print(pumpTiming)
    acknowledgeRecipe(database.child(ID))
    print(f"Entered critical section.")

    # block other accounts from using the machine
    lockDispenser(database.child(ID))

    initialLevels = getLiquidLevels(database)
    print(initialLevels)
    
    # Begin initial liquid dispensing using the motors
    for m, pTime in pumpTiming.items():
        motors[m].pour(pTime)

    # Wait for the motors to stop
    while any(motors[m].is_active for m in pumpTiming.keys()):
        sleep(WAIT)
    
    # Feedback not required for simulation, assuming ideal

    print("Pumping complete. Releasing critical section.")
        
    # unblock other accounts from using the machine
    unlockDispensing(database.child(ID))
    
async def loop(motors: dict[str, LiquidPump], database: Database):    
    makeDrinkBind = partial(drinkMaker, motors = motors, database = database)
    while True:
        
        makeDrink = database.child(MOCKTENDER_CONFIG.getId()).child(
            RECIPE).stream(makeDrinkBind, is_async=True)
        try:
            await asyncio.wait([makeDrink], timeout=30)
        except asyncio.TimeoutError:
            print("loop @ ln65: Timed out")  
            


def main(PROD: bool):
    CONFIG = CONFIG_PROD if PROD else CONFIG_DEV
    PINS = MOCKTENDER_CONFIG.getPins()

    motorVals = LiquidPump(forward=PINS[0]), LiquidPump(
        forward=PINS[1]), LiquidPump(forward=PINS[2])
    motorKeys = FIREBASE_MOTOR_NAMES.copy()

    MOTORS = dict(zip(motorKeys, motorVals))

    firebase = initApp(CONFIG)
    db = firebase.database()

    asyncio.run(loop(MOTORS, db))
    
    
if __name__ == "__main__":
    main(True if len(argv) > 1 else False)
