from gpiozero import DigitalOutputDevice

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

ML_CONVERSION = 100  # conversion factor for milliliters

class LiquidPump(DigitalOutputDevice):
    def __init__(self, forward, active_high=True, initial_value=False, pin_factory=None):
        super().__init__(pin=forward, active_high=active_high,
                         initial_value=initial_value, pin_factory=pin_factory)

    def pour(self, seconds: float):
        self.blink(seconds, 1, n=1, background=True)

    @classmethod
    def convertPercentToSeconds(self, liquidPercentage,
                                totalVolume) -> float:
        '''
        Converts the percentage of the liquid in the drink to the volume of
        that liquid using the totalVolume as a reference. Using that volume,
        the known flow rate of the pump will be used to convert it to the
        number of seconds required to pump.

        Returns -1 if the percentage of the liquid is less than 0 or greater
        than 100
        '''
        if (DRINK_PERCENTAGE_MIN > liquidPercentage > DRINK_PERCENTAGE_MIN):
            return -1

        liquidVolume = (liquidPercentage / ML_CONVERSION) * totalVolume  # mL
        numPumpSeconds = (liquidVolume / FLOW_RATE) * 60

        return round(numPumpSeconds, SIG_FIGS)

    @classmethod
    def convertSecondsToVolume(self, pumpSeconds) -> float:
        return (pumpSeconds / 60) * FLOW_RATE
		
    @classmethod
    def validateRecipe(self, recipe: dict) -> dict[str, float]:
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

        INVALID_RECIPE = {"l1": None}

        # recipe and recipe members are None
        if (recipe is None):
            return INVALID_RECIPE
        if (recipe[DRINK_SIZE] is None or recipe[DRINK_PERCENTAGES] is None):
            return INVALID_RECIPE

        percentagesDict: dict = recipe.get(DRINK_PERCENTAGES)
        percentages = list(percentagesDict.values())
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

        actuators = "l1,l2,l3".split(",")
        actuatorTimeMap = {}
        for percent in percentages:
            actuatorTimeMap[actuators.pop(0)] = self.convertPercentToSeconds(percent, drinkSize)

        return actuatorTimeMap
