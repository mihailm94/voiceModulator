#main file to call all the other modules

#GPIO
import RPi.GPIO as GPIO
import time
import signal
import subprocess

RESET_BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RESET_BUTTON, GPIO.IN)

#activate killall "watchdog"
#watchdog = subprocess.Popen('pkill -f resetProcess.py', shell=True)

#time.sleep(2)

#watchdog = subprocess.Popen('python resetProcess.py', shell=True)


#poll all the time for incoming button presses
state = GPIO.input(RESET_BUTTON)

while state:
    
        
    
    print("test")
    time.sleep(1)




#subprocess.Popen('kill -9 `ps -ef | pgrep resetProcess.py`', shell=True)
GPIO.cleanup()

