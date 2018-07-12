#main file to call all the other modules

#LIBRARIES
import RPi.GPIO as GPIO
import time
import signal
import subprocess
import sys

#SERIAL
import serial

#MODULES (in dir modules)
sys.path.append('./modules')
import record
import effectChain

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

#effects array
effects = []

while True:
    #poll serial port (byte read)
    read_key = serial.read()
    
    #if key = A, start recording
    if(read_key == 'A'):
        record.startRec(read_key)
        
        #subprocess.Popen('cp ./audioFiles/file.wav ./audioFiles/fileCopy.wav', shell=True)

    #if key = B, terminate recording
    elif(read_key == 'B'):
        record.startRec(read_key)
    
    #volumeup
    elif(read_key == 'C'):
        #volumeup
        print("volup")

    #volumedown
    elif(read_key == 'D'):
        #volumedown
        print("voldown")    
        
    elif(read_key == '1'):
        #reverb
        #append to effect array
        effects.append(".reverb()")
        print("append reverb to array")

    elif(read_key == '2'):
        #delay
        #append to effects array
        effects.append(".delay()")
        print("appended delay to effects") 


    #apply selected effect
    elif(read_key == 'E'):
        
        #cast array to single string
        effStr = ''.join(effects)
        effectChain.writeFile(effStr)
        
        #os.system('python ./modules/effectApply2.py')
        
        print("success")

    elif(read_key == 'F'):
       
        subprocess.Popen('aplay ./audioFiles/modulated.wav', shell=True)


#subprocess.Popen('kill -9 `ps -ef | pgrep resetProcess.py`', shell=True)

