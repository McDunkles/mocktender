import json
'''
This is a wrapper class for dbFormat.json, as well as a convenient
way to access the Firebase credentials.

Author: Ethan Bradley, 101158848
'''

class MocktenderConfig():

    CONFIG_PROD = {
        "apiKey": "AIzaSyCKWbxmg1GfOKYSaY3Ioc_1f7vRWrbiejw",
        "authDomain": "mocktenderdb.firebaseapp.com",
        "databaseURL": "https://mocktenderdb-default-rtdb.firebaseio.com/",
        "storageBucket": "mocktenderdb.appspot.com"
    }

    CONFIG_DEV = {
        "apiKey": "your-dev-server-api-key",
        "authDomain": "your-dev-server.firebaseapp.com",
        "databaseURL": "https://your-dev-server-default-rtdb.firebaseio.com/",
        "storageBucket": "your-dev-server.appspot.com"
    }

    _ID = "id"
    _STRUCTURE = "structure"
    _CONFIG_PATH = "./dbFormat.json"
    _PINS = "pins"

    def __init__(self) -> None:
        self._dbFormat = {}
        with open(self._CONFIG_PATH, "r") as j:
            self._dbFormat = dict(json.load(j))
        
        self._id = self._dbFormat[self._ID]
        self._pins: list[int] = []
        pins = list(self._dbFormat[self._PINS])
        for pin in pins:
            self._pins.append(int(pin))

        self._structure = dict(self._dbFormat[self._STRUCTURE])
    
    def getId(self) -> str:
        return self._id

    def getPins(self) -> tuple[int]:
        return tuple(self._pins)

    def getStructure(self) -> dict:
        return self._structure
	