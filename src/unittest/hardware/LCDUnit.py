"""
Unit test for the LCD hardware
Tests each individual character and
all characters at once.

Author: Matt Reid
"""

from time import sleep
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

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

# Wipe the LCD before starting the test
lcd.clear()

# Test that each individual character works by scrolling the number 8
lcd.message = "8"
sleep(0.25)
for i in range(17):
    lcd.move_right()
    sleep(0.25)

lcd.clear()

lcd.message = "\n8"
sleep(0.25)
for i in range(17):
    lcd.move_right()
    sleep(0.25)

lcd.clear() # Reset the LCD

# Test that all 32 characters can display at once
lcd.message = "1234567891234567\n1234567891234567"
sleep(10)

lcd.clear() # Reset the LCD

# Test messages from the Mocktender System
lcd.message = "Mocktender\nTurning On"
sleep(5)

lcd.clear() # Reset the LCD

lcd.message = "Dispensing:\nTest Recipe"
sleep(5)

lcd.clear() # Reset the LCD

lcd.message = "Out of Liquid:\nLiquid Name"
sleep(5)

lcd.clear() # Reset the LCD

lcd.message = "Error 1:\nConnection Lost"
sleep(5)

lcd.clear() # Reset the LCD


