"""
Hardware unit test for pumps.
Tests running a peristaltic pump.

Author: Ethan Bradley
"""

from gpiozero import Motor
from time import sleep


class LiquidPump():

    def __init__(self, forwardPin=17, backwardsPin=18):
        self.motor = Motor(forward=forwardPin, backward=backwardsPin, pwm=True)
        self.dutyCycle = 0

    def setDutyCycle(self, dutyCycle: int):
        self.dutyCycle = dutyCycle

    def startMotor(self, timeout=60):
        self.__rampUp()
        sleep(timeout)
        self.__rampDown()

    def __rampUp(self):
        print("ramping up")
        currentDutyCycle = 0
        while (currentDutyCycle < self.dutyCycle):
            currentDutyCycle += 0.05
            self.motor.forward(min(currentDutyCycle, 1))
            sleep(0.1)
        
        self.motor.forward(self.dutyCycle)

    def __rampDown(self):
        print("ramping down")
        currentDutyCycle = self.dutyCycle
        while (currentDutyCycle > 0):
            currentDutyCycle -= 0.05
            self.motor.forward(max(currentDutyCycle, 0))
            sleep(0.1)
        
        self.motor.stop()

if __name__ == "__main__":
    d = LiquidPump()
    d.setDutyCycle(1)
    d.startMotor(timeout=5)
