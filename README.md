# L3-G8 Mocktail Mixing Machine Project

![Mocktender Title Image](/diagrams/Mocktender.png)

## Team Members:
The Mocktender was developped in Winter 2023 for the SYSC 3010 class by:
- Matt Reid
- Ethan Bradley
- Duncan MacLeod

#### TA: Roger Selzler

## About the Project
A mocktail is a non-alcoholic drink that captures the essence of a cocktail without the downsides of alcohol consumption. From work offices where you want to stay sharp while having fun drinks for lunch to wanting a healthier alternative to drinking cocktails at home. To provide the ease of having drinks at home or private events without needing to buy equipment and learn how to mix them yourself or paying a bartender, the Mocktender will provide the ability to create mocktails at home with ease. 

The Mocktender provides a web interface GUI that can be used to remotely view liquid levels, add recipes, change settings, and dispense drinks. Our project has three raspberry pi devices, one for the user interface, one for the machine (IOController), and one to simulate a second machine. The machine itself has a Raspberry Pi control device which is connected by GPIO to ultrasonic sensors to get the liquid level in real time. When a recipe is specified, it is sent through a Firebase real time database to the control device which runs peristaltic pumps to dispense the drink. An LCD displays output to the user of the machine showing the status of the machine.

## Contents
The contents of the top level directories are as follows:
- [/src](/src): Source code for the Mocktender including tests
- [/diagrams](/diagrams): Diagrams/Images used in Mocktender documentation and reports
- [/WIPUR](/WIPUR): Weekly Individual Projecet Update Reports
- [/3D_models](/3D_modles): 3D models for the liquid pump system (not used in final version)
- [/schematics](/schematics): Schematics used in Mocktender documentation and reports

The SRC (source code) folder contains the following directories:
- [/src/IOController](/src/IOController): Code for the IOController node which represents the real Mocktender machine
- [/src/SystemSimulator](/src/SystemSimulator): Code for the SystemSimulator node which simulates a Mocktender machine
- [/src/UserInterface/mkt-ui](/src/UserInterface/mkt-ui): Code for the UserInterface node which runs the Web Interface
- [/src/mkt-persistance](/src/mkt-persistane): Code for the persistance layer of the UserInterface node
- [/src/end2end](/src/end2end): Code and testing plan for the end to end test demonstration
- [/src/unittest](/src/unittest): Unit tests for the Mocktender machine. Includes the unit testing demo plan

## Installation
### Hardware

#### Electronics Necessary 
To build the hardware components of a Mocktender, the following components will be required:
- 1x Raspberry Pi 4B
- 3x UltraSonic Sensor
- 3x Peristaltic Pumps
- 2x L298N Dual H-Bridge driver
- 1x 1602A LCD Module
- 4x 220Ω resistor
- 3x 330Ω resistor
- 1x 2.2KΩ resistor
- 2x 9V rechargeable batteries

For documentation on how to connect these components together, please refer to Section 4 of the [Detailed Design Document](/documents/SYSC3010-TheMocktenderDetailedDesign-L3G8.pdf)

Food grade silicone hosing will also be required for pumping the liquid from the internal containers to a choice of reservoir.

### Software
#### Dependencies
A number of libraries need to be installed for a Mocktender to work.
The following commands can be used to install the necessary libraries (You may have to use `sudo` to install these properly):

```
python3 -m pip install pyrebase
python3 -m pip install gpiozero
python3 -m pip install adafruit-circuitpython-charlcd
```


#### Firebase Configuration
To begin getting the software all setup for a Mocktender, a Firebase Real-Time Database would need to be created for the user. The credentials for the project need to be filled out in [MocktenderConfig.py](/src/IOController/MocktenderConfig.py) as can be seen below:

```python
CONFIG_PROD = {
        "apiKey": "your-firebase-project-api-key",
        "authDomain": "your-firebase-project.firebaseapp.com",
        "databaseURL": "https://your-firebase-project-rtdb.firebaseio.com/",
        "storageBucket": "your-firebase-project.appspot.com"
}
```
In [dbFormat.json](/src/IOController/dbFormat.json), fill out the id value to be a name of your choosing.

```json
{
	"id": "device id name"
}
```
At the root of the project repo, the user should run the following commands

```bash
cd src/IOController/
python3 MocktenderRegistration.py production
```

This will upload the necessary schema to the Firebase Real-Time Database to run the Mocktender.

#### Email Notification Configuration 
The Mocktender also has email notification sending capabilities. To be able to use this functionality properly, please refer to [this repository](https://github.com/Brethan/ipy-mailer) for detailed instructions on how to set up an email for SMTP purposes.

In [notif_config.json](src/IOController/mailer/notif_config.json), use the values from the aforementioned instructions and paste them in this file.

```json
{
	"app_pw": "app-password",
	"sender": "your-python-smtp-email@gmail.com",
	"sender_name": "Mocktender"
}
```
## Usage
#### IOController Deployment
The IOController of the Mocktender can now be deployed by running the following commands at the root of the project directory:
```bash
cd src/IOController/
python3 IOLiquidLevel.py & python3 IOController.py production &
```

You should see IO device related errors due to IOLiquidLevel.py, followed by decimal numbers which are the 
measured liquid levels from the UltraSonic sensors. If one is paying attention to the Firebase RTDB,
they will noticed that there will be timestamped liquid levels being added to it.

Additionally, there will be errors from IOController.py due to issues with the asyncio API. The LCD screen
should say "Mocktender Ready" once it has been initialized.

The errors will not affect the runtime of the Mocktender.
## The Mocktender Machine
![Mocktender Machine](/diagrams/MocktenderSystem.png)

## UML Deployment Diagram

![UML Deployment Diagram](/diagrams/DeploymentDiagram.png)

## Project Milestones

| Milestone # | Name | Description |
| ------------| -----| ------------ |
| 1 | Uploading and Fetching Data | Computer devices can read from and write data to a real-time database independently of each other, which can then be accessed and displayed on an external device. |
| 2 | Communication Between Nodes | Communication established between computer devices (HTTP etc.) to transfer data stored locally between nodes and issue commands. |
| 3 | Measurement and Conditional Actuation | Liquid level of a fixed container can be measured accurately using sensors can uploaded to the database. Data can be used to turn on an LED when a threshold is reached. |
| 4 | Exposing Data to the World | Two additional containers with liquid level measuring will also have their data uploaded to the database. The liquid level will be displayed as text on a webserver |
| 5 | Hardware Assembly | Assembled liquid dispensing system utilizing peristaltic pumps. Liquid level on webserver should be updated (as text) in real-time. |
| 6 | Graphical User Interface | Webserver displays the volume of the liquid containers as an animation. Users can navigate between different webpages on the server. |
| 7 | Controlling the Hardware System with UI | Webserver component can control all 3 liquid pumps implementing the drink mixing. Users can login and save customs mixtures locally and in the real-time database. |
