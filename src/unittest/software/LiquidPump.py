from gpiozero import Motor
from time import sleep

'''
This class is meant to control the rate at which the pump
pumps liquid at as well as calculate how long to pump liquid
for based on the size of a drink, the percentage of a liquid
of the drink, and the known flow rate of the pump

Author: Ethan Bradley, 101158848
'''

FLOW_RATE = 100  # mL per minute
DRINK_SIZE = "drinkSize"
DRINK_PERCENTAGES = "drinkPercentages"

DRINK_PERCENTAGE_MAX = 100
DRINK_PERCENTAGE_MIN = 0
DRINK_SIZE_MIN = 0

SIG_FIGS = 3  # number of figures to round to

RAMP_RATE = 0.05  # how much to increase the speed per ramp
RAMP_DELAY = 0.1  # how often the motor ramps
RAMP_MIN = 0  # minimum speed for the motor
RAMP_MAX = 1  # maximum speed for the motor

DEF_FORWARD_PIN = 17  # default forwards pin
DEF_BACKWARDS_PIN = 18  # default backwards pin

ML_CONVERSION = 100  # conversion factor for milliliters


class LiquidPump():
    def __init__(self, forward=DEF_FORWARD_PIN, backwards=DEF_BACKWARDS_PIN):
        self.motor = Motor(forward=forward, backward=backwards, pwm=True)
        self.dutyCycle = RAMP_MIN

    def setDutyCycle(self, dutyCycle: int) -> None:
        self.dutyCycle = dutyCycle

    def runPump(self, timeout=60) -> None:
        '''
        turns the motor on for some timeout value with a default of 60 seconds
        and then ramps down the motor to 0 speed
        '''
        self.__rampUp()
        sleep(timeout)
        self.__rampDown()

    def convertPercentToMinutes(self, liquidPercentage,
                                totalVolume) -> float:
        '''
        Converts the percentage of the liquid in the drink to the volume of
        that liquid using the totalVolume as a reference. Using that volume,
        the known flow rate of the pump will be used to convert it to the
        number of minutes required to pump.

        Returns -1 if the percentage of the liquid is less than 0 or greater
        than 100
        '''
        if (DRINK_PERCENTAGE_MIN > liquidPercentage > DRINK_PERCENTAGE_MIN):
            return -1

        liquidVolume = (liquidPercentage / ML_CONVERSION) * totalVolume  # mL
        numPumpMinutes = liquidVolume / FLOW_RATE

        return round(numPumpMinutes, SIG_FIGS)

    def validateRecipe(self, recipe: dict) -> tuple[float, float, float]:
        '''
        Takes in a recipe from the backend server and converts it to the
        amount of time that the pumps would need to run to create the
        recipe.
        If the recipe is invalid (None values, sum(percentages) > 100,
        negative percentages) the method should return a tuple containing None.

        Example 1 (no issues):
        >>> recipe = {DRINK_SIZE: 15, DRINK_PERCENTAGES: [25, 25, 50]}
        >>> actualResult = LiquidPump.validateRecipe(recipe)
        >>> expectedResult = (0.062, 0.062, 0.125)
        >>> print(compare(actualResult, expectedResult)) # true

        Example 2 (negative size and percentage, sum(percentages) > 100):
        >>> recipe = {DRINK_SIZE: -25, DRINK_PERCENTAGES: [25, 150, -50]}
        >>> actualResult = LiquidPump.validateRecipe(recipe)
        >>> expectedResult = (None,)
        >>> print(compare(actualResult, expectedResult)) # true
        '''

        INVALID_RECIPE = (None,)

        # recipe and recipe members are None
        if (recipe is None):
            return INVALID_RECIPE
        if (recipe[DRINK_SIZE] is None or recipe[DRINK_PERCENTAGES] is None):
            return INVALID_RECIPE

        percentages = recipe[DRINK_PERCENTAGES]
        drinkSize = recipe[DRINK_SIZE]

        # drinkSize is negative
        if (drinkSize <= DRINK_SIZE_MIN):
            return INVALID_RECIPE
        # Percentages are negative
        if any(percent < DRINK_PERCENTAGE_MIN for percent in percentages):
            return INVALID_RECIPE
        # Percentages sum to over 100%
        if sum(percentages) > DRINK_PERCENTAGE_MAX:
            return INVALID_RECIPE

        pumpTimes = []  # store the conversions in a list
        for percent in percentages:
            pumpTimes.append(self.convertPercentToMinutes(percent, drinkSize))

        return tuple(pumpTimes)

    def __rampUp(self):
        '''
        Ramps up the speed of the motor up to set duty cycle value.
        Does not change the value of the motor's duty cycle
        '''
        print("ramping up")
        currentDutyCycle = RAMP_MIN
        while (currentDutyCycle < self.dutyCycle):
            currentDutyCycle += RAMP_RATE
            self.motor.forward(min(currentDutyCycle, RAMP_MAX))
            sleep(RAMP_DELAY)

        self.motor.forward(self.dutyCycle)

    def __rampDown(self):
        '''
        Ramps down the speed of the motor until it completely stops.
        Does not change the value of the motor's duty cycle.
        '''
        print("ramping down")
        currentDutyCycle = self.dutyCycle
        while (currentDutyCycle > RAMP_MIN):
            currentDutyCycle -= RAMP_RATE
            self.motor.forward(max(currentDutyCycle, RAMP_MIN))
            sleep(RAMP_DELAY)

        self.motor.stop()
