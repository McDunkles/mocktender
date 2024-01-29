from firebase_config_e2e import init_config
from time import sleep
from requests.exceptions import HTTPError


class RPi_Node():
    '''
    Represents a Raspberry Pi. Our system uses Firebase to communicate between
    Raspberry Pis.

    The schema in Firebase is non-relational and resembles a JSON-like
    structure. Below is an illustration of how it looks. "UserInterface",
    "IOController", and "SystemSimulator" are the names given to each
    Raspberry Pi based on their function in our system.

    {
        "UserInterface": {
            "IOController": [],
            "SystemSimulator": []
        },
        "IOController": {
            "UserInterface": []

        },
        "SystemSimulator": {
            "UserInterface": []
        }
    }

    So, the idea here would be to initialize three RPi_Node objects using the
    three names mentioned above, and send/receive messages via the send() and
    receive() methods.
    '''

    def __init__(self, name):
        '''
        Initializes an RPi_Node object
        '''
        self.name = name

        # init_config() is a method imported from a different source file. It
        # specifies the apiKey, domain, and other required fields to create a
        # Firebase object, defined in the 'pyrebase' library
        self.firebase = init_config()
        self.db = self.firebase.database()

    def testConnectivity(self) -> bool:
        '''
        Tests the connectivity of a node to the Firebase
        real-time database which is being used as the backend

        Returns True if the connection is successful, False otherwise.
        '''

        can_connect = True

        try:
            # Try to connect to the database
            self.db.get()
        except HTTPError:
            can_connect = False

        return can_connect

    def send_message(self, message, rpi_dest) -> bool:
        '''
        Writes a message into the database.

        'rpi_dest' is a RPi_Node object. The destination in the database to
        write the message in is specified by the 'name' field of rpi_dest.

        Returns True if the message is sent successfully, False otherwise.
        '''

        db_child = rpi_dest.name

        msg_sent = True

        try:
            # Tries to set the value at the 'db_child' node
            self.db.child(db_child).set(message)
        except HTTPError:
            msg_sent = False

        return msg_sent

    def receive_message(self) -> dict:
        '''
        Receives a message at the destination given by this object's 'name'
        field.

        Returns the received message as a Python dictionary.
        '''

        # Specifies the node in the database to receive the message from
        db_child = self.name

        received_message = None

        # Simple procedure to poll the database at the specified node for a
        # short amount of time to ensure that a sent message is received.
        # Using this configuration, the node will be polled at a rate of
        # 5 times/second, for 20 seconds. The main polling loop will exit if a
        # value is received at any point OR the poll limit has been reached
        timeout, count = 100, 0
        poll_frequency = 5

        # Specify sleep time based on the polling frequency
        sleep_duration = (1/float(poll_frequency))

        while ((received_message is None) and (count > timeout)):

            received_message = self.db.child(db_child).get().val()
            sleep(sleep_duration)
            count += 1

        return {"0": received_message}
