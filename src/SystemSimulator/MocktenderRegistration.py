from pyrebase import initialize_app as initApp
from SystemSimulator.MocktenderConfig import MocktenderConfig
from sys import argv
'''
The purpose of this file is to create a new Firebase Real-Time Database
schema for a Mocktender that is running for the first time.

Author: Ethan Bradley, 101158848
'''


def registerMocktender(PROD):
    '''
    Creates a new tree in the Firebase RTDB that matches the exact
    format required for this project under the devices ID name
    '''
    MOCK = MocktenderConfig()

    ID = MOCK.getId()
    STRUCTURE = MOCK.getStructure()

    # select production or development environment
    fbConfig = MOCK.CONFIG_PROD if PROD else MOCK.CONFIG_DEV

    db = initApp(fbConfig).database()
    db.child(ID).set(STRUCTURE)


if __name__ == "__main__":
    registerMocktender(True if len(argv) > 1 else False)
