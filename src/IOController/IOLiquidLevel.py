"""
Main file for the Liquid Level system on the IOController.
Initalizes ultrasonic sensor and liquid level system objects
that are used to send liquid levels to the mocktender db Firebase
real time database every 10 seconds. The measurements are taken
every second and the median is taken to account for variation
in the sensor output (tolerance is 5mm).

Author: Matt Reid
"""
from UltrasonicSensor import UltrasonicSensor
from LiquidLevelSystem import LiquidLevelSystem
from pyrebase.pyrebase import Database
from threading import Thread
import mailer.NotifyCustomer as mailer
import time
import board
import digitalio
import pyrebase
import os
import json
import statistics
import adafruit_character_lcd.character_lcd as characterlcd

DB_USERNAME = "IOController"
LIQUID1_DATASET = "LiquidLevel1"
LIQUID2_DATASET = "LiquidLevel2"
LIQUID3_DATASET = "LiquidLevel3" 
NOTIFIED = "notified"
DATASETS = [LIQUID1_DATASET, LIQUID2_DATASET, LIQUID3_DATASET]
CONFIG = json.loads(os.environ['MOCKTENDERDBCONFIG'])
VALUE = 40  # Value to round liquid measurement to
# notify machine owner when liquid level dips below threshold
THRESHOLD = VALUE 

if __name__ == '__main__':

    # LCD is 16 columns by 2 rows
    lcd_columns = 16
    lcd_rows = 2

    # Declare the pins used for the LCD
    lcd_rs = digitalio.DigitalInOut(board.D23)
    lcd_en = digitalio.DigitalInOut(board.D18)
    lcd_d4 = digitalio.DigitalInOut(board.D22)
    lcd_d5 = digitalio.DigitalInOut(board.D17)
    lcd_d6 = digitalio.DigitalInOut(board.D27)
    lcd_d7 = digitalio.DigitalInOut(board.D4)

    # Initialise the lcd class
    lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                        lcd_d7, lcd_columns, lcd_rows)

    # Clear the LCD
    lcd.clear()

    # Display startup message
    lcd.message = "Mocktender\nPowering On"

    # Init ultrasonic sensors to their pins (echo,trigger)
    sensor1 = UltrasonicSensor(21,20)
    sensor2 = UltrasonicSensor(12,16)
    sensor3 = UltrasonicSensor(24,25)

    # Init the liquid level system with the sensors
    liquid_system = LiquidLevelSystem(sensor1,sensor2,sensor3)

    # Init the database with the config
    firebase = pyrebase.initialize_app(CONFIG)
    db = firebase.database()

    time.sleep(2)

    # Periodic timing loop
    while True:
        # Get the current time to use as a child
        dtime = time.strftime("%Y-%m-%d %H:%M:%S")

        # Get 10 volume measurements to get the median measurement
        count = 0
        volume_list_1 = []
        volume_list_2 = []
        volume_list_3 = []
        
        # Get 10 measurements 1 second apart
        while count < 10:
            volume_list_1.append(liquid_system.get_volume_from_sensor(1, VALUE))
            volume_list_2.append(liquid_system.get_volume_from_sensor(2, VALUE))
            volume_list_3.append(liquid_system.get_volume_from_sensor(3, VALUE))
            count += 1
            time.sleep(1)

        print(volume_list_1)
        print(volume_list_2)
        print(volume_list_3)
        print("\n")
        
        # Get the medians of the 10 measurements to imporve accuracy (average could cause problems)
        median_vol_1 = statistics.median(volume_list_1)
        median_vol_2 = statistics.median(volume_list_2)
        median_vol_3 = statistics.median(volume_list_3)
        
        # Upload liquid level to DB
        db.child(DB_USERNAME).child(LIQUID1_DATASET).child(dtime).set(median_vol_1)
        db.child(DB_USERNAME).child(LIQUID2_DATASET).child(dtime).set(median_vol_2)
        db.child(DB_USERNAME).child(LIQUID3_DATASET).child(dtime).set(median_vol_3)

        #lcd.message = ("Median 1:\n %d" % median_vol_1)
        median_vols = [float(median_vol_1), float(median_vol_2), float(median_vol_3)]
        belowThreshold: list[int] = []
        aboveThreshold: list[int] = []
            
        # Check if a volume is less than the threshold (to send notification
        for i, vol in enumerate(median_vols):
            if vol <= THRESHOLD:
                belowThreshold.append(i)
            else:
                aboveThreshold.append(i)
            pass
        
        # If the user needs to be notified, get the db user to notify
        liquidsToNotify: list[str] = []
        for i in belowThreshold:
            dataset = DATASETS[i]
            userNotified: bool = db.child(DB_USERNAME).child(NOTIFIED).child(dataset).get().val()
            if not userNotified:
                liquidsToNotify.append(f"Liquid {i + 1}")
                db.child(DB_USERNAME).child(NOTIFIED).child(dataset).set(True)
            
        for i in aboveThreshold:
            dataset = DATASETS[i]
            db.child(DB_USERNAME).child(NOTIFIED).child(dataset).set(False)

        # If sending a notification, create it and email it to the user
        if len(liquidsToNotify) > 0:
            subject = "Mocktender Low Volume Notification"
            content = "Warning - the following liquids in your Mocktender are low:"
            content += str(liquidsToNotify)
            recipient = db.child(DB_USERNAME).child("email").get().val()
            thr = Thread(target=mailer.__send_email, args=[content, subject, recipient])
            thr.start()




