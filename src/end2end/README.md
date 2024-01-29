# L3-G8 End-to-End Testing Demonstration
### Completed on March 10th, 2023

## Testing Plan
The Mocktender machine consists of multiple Raspberry Pi devices that need to communicate amongst each other to meet our project goals. The system is distributed between the Pi devices with one device hosting the front-end web interface for viewing the state of the machine and controlling the hardware devices. The User Interface device is responsible for updating the Firebase database with the liquid level sensor data and sending the signals to the hardware devices. The Sensor System and Simulation devices perform the same communication, so only one of them needs to be tested in end-to-end testing.
     To test the end-to-end communication between the components, all the messages discussed in Section 2.1 will need to be created. The test scripts created will generate the messages, send them to the correct end destination, and the end destination will confirm that the message was received, and the contents are as expected. The test will pass if the message is the same as was expected, and will fail if either no message was received, or the contents are different than was expected. To provide test feedback, the messages will be printed to a console that will also be available on the Raspberry Pi devices whenever needed as a debugging option. The database contents on the Firebase real time database will also be tested after the messages are sent to ensure that the contents are as expected.

The following steps will be performed in our end-to-end testing demonstration:
1. First, the connections between the Raspberry Pi devices, and the Firebase real time database will be tested. A test script will verify that all of the Pi devices are able to connect to the Firebase server.
2. Next, messages will be sent between Pi devices over the Firebase database to demonstrate that messages can be sent and received through that database.
3. Finally, a Flask web server will be created to demonstrate that a button press can send a message from the user interface pi to the Firebase database.
