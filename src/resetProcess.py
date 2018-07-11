#ifndef resetProcess.py

#this module sends a kill command to the processes
#restarts the main.py after a certain delay

import RPi.GPIO as GPIO
import time
import signal
import subprocess

#GPIO 17 is the button GPIO on the board itself
BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

#killCommand = "kill `ps -ef | pgrep -f main.py` "
#startCommand = "python main.py"

state = GPIO.input(BUTTON)

while True:
    #poll GPIO
    state = GPIO.input(BUTTON)

    if not state:
        killProcess = subprocess.call('kill -9 `ps -ef | pgrep -f main.py`', shell=True)
        killProcess.terminate()
        print("process killed, restarting")
        
        time.sleep(1)
       
        restartProcess = subprocess.call('python main.py', shell=True)
        
        time.sleep(1)
        #killSelf = subprocess.Popen('kill -9 `ps -ef | pgrep -f resetProcess.py`', shell=True)

        print("restart successful")

