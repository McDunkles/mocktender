from LiquidPump import LiquidPump
'''
This file is to provide software to test the functionality
of the liquid pump hardware
Author: Ethan Bradley, 101158848
'''
FORWARD_PIN = 17
BACKWARD_PIN = 18
MAX_DUTY_CYCLE = 1
ACCEPTABLE_ERROR = 10
ON_TIME = 30

MEASURING_CUP_VOLUME = 250


def testPumpFlowRate(pump: LiquidPump, expectedVolume: int):
    '''
    Ramps up the motor speed to begin pumping the liquid into a measuring cup.
    The user will verify manually the volume indicated by the measuring cup.

    If the expectedVolume - actualVolume < ACCEPTABLE_ERROR the unit has
    passed.
    '''

    pump.startMotor(timeout=ON_TIME)
    # prompt user for the actual pumped volume
    actualVolume = int(input("Enter the volume as indicated on the pyrex:"))
    if (abs((expectedVolume - actualVolume)) < ACCEPTABLE_ERROR):
        print(
            f"\nTEST PASS: Within {ACCEPTABLE_ERROR}mL of expected volume")
    else:
        print(f"\nTEST FAIL: Outside the {ACCEPTABLE_ERROR} "
              + "mL tolerance threshold.")


def main():
    '''
    
    '''
    
    pump = LiquidPump(forwardPin=FORWARD_PIN, backwardsPin=BACKWARD_PIN)
    pump.setDutyCycle(MAX_DUTY_CYCLE)

    print(f"Testing DC Motor Pump using {MEASURING_CUP_VOLUME}"
          + "mL measuring cup.")

    expectedVolume1 = (MEASURING_CUP_VOLUME / 5)
    input("\n\nTest 1: Ensure that the pyrex is" +
          "empty and press enter to start...\n")
    testPumpFlowRate(pump, expectedVolume1)

    expectedVolume2 = expectedVolume1 * 2
    input("\n\nTest 2: Ensure the pyrex is filled" +
          f" to the {expectedVolume1}mL line and press enter to continue...\n")
    testPumpFlowRate(pump, expectedVolume2)

    expectedVolume3 = expectedVolume1 * 3
    input("\n\nTest 3: Ensure the pyrex is filled" +
          f" to the {expectedVolume2}mL line and press enter to continue...\n")
    testPumpFlowRate(pump, expectedVolume3)

    expectedVolume4 = expectedVolume1 * 4
    input("\n\nTest 4: Ensure the pyrex is filled" +
          f" to the {expectedVolume3}mL line and press enter to continue...\n")
    testPumpFlowRate(pump, expectedVolume4)

    expectedVolume5 = expectedVolume1 * 5
    input("\n\nTest 5: Ensure the pyrex is filled" +
          f" to the {expectedVolume4}mL line and press enter to continue...\n")
    testPumpFlowRate(pump, expectedVolume5)

    pass


if __name__ == "__main__":
    main()
