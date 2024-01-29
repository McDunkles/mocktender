import pyrebase


def init_config():
    config = {
        "apiKey": "AlzaSyBugZNEeK_HK1534mP9RUw0HS0c-KfhLqw",
        "authDomain": "mocktenderdb.firebaseapp.com",
        "databaseURL": "https://mocktenderdb-default-rtdb.firebaseio.com/",
        "storageBucket": "mocktenderdb.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    return firebase
