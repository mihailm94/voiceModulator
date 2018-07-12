#main file to call all the other modules

#LIBRARIES
import RPi.GPIO as GPIO
import time
import signal
import subprocess

#SERIAL
import serial

#MODULES (in dir modules)
import sys
sys.path.append('./modules')
import record

#Button on 
RESET_BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RESET_BUTTON, GPIO.IN)

#activate killall "watchdog"
#watchdog = subprocess.Popen('pkill -f resetProcess.py', shell=True))

#watchdog = subprocess.Popen('python resetProcess.py', shell=True)


#poll all the time for incoming button presses
state = GPIO.input(RESET_BUTTON)

#set up usb connection to arduino/nodemcu , baudrate = 9600
serial = serial.Serial('/dev/ttyUSB0', 9600)



while True:
    #poll serial port (byte read)
    read_key = serial.read()
    
    #if key = A, start recording
    if(read_key == 'A'):
        record.startRec(read_key)
        

    #if key = B, terminate recording
    elif(read_key == 'B'):
        record.startRec(read_key)


    elif(read_key == '1'):
        applyEffects(1)

    elif(read_key == '2'):
        applyEffects(2)
    
    

    elif(read_key == 'F'):



#subprocess.Popen('kill -9 `ps -ef | pgrep resetProcess.py`', shell=True)

