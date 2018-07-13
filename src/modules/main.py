#main file to call all the other modules

#LIBRARIES
import RPi.GPIO as GPIO
import time
import signal
import subprocess
import sys
import os
#SERIAL
import serial

#MODULES (in directory modules)
#sys.path.append('./modules')
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
effects = ['']


print("welcome to VoiceModulator")


while True:
    #poll serial port (byte read)
    read_key = serial.read()
    
    #if key = A, start recording
    if(read_key == 'A'):
        print("recording")
        record.startRec(read_key)
        
    #if key = B, terminate recording
    elif(read_key == 'B'):
        print("rec interrupt")
        #record.startRec(read_key)
        subprocess.Popen('sudo killall ffmpeg', shell = True)

    #volumeup
    elif(read_key == 'C'):
        #volumeup
        print("volup")
        subprocess.Popen('amixer -c1 sset \'Speaker\' 5%+', shell = True)

    #volumedown
    elif(read_key == 'D'):
        #volumedown
        print("voldown")    
        subprocess.Popen('amixer -c1 sset \'Speaker\' 5%-', shell = True)
                
        
    elif(read_key == '1'):
        #reverb
        #append to effect array
        effects.append(".reverb()")
        print("reverb")

    elif(read_key == '2'):
        #delay
        #append to effects array
        effects.append(".delay()")
        print("delay") 
    
    elif(read_key == '3'):
        #phaser

        #does not function properly
        effects.append(".phaser()")
        print("phaser")

    elif(read_key == '4'):
        #pitch up
        effects.append(".pitch(1400, True)")
        print("pitch up")
    
    elif(read_key == '5'):
        #pitch down
        effects.append(".pitch(-750, True)")
        print("pitch down")
    
    elif(read_key == '6'):
        #reverse
        effects.append(".reverse()")
        print("reverse")
        
    elif(read_key == '7'):
        effects.append(".speed(2)")
        print("speed")

    elif(read_key == '8'):
        effects.append(".tremolo(4000)")
        print("tremolo")

    elif(read_key == '9'):
        effects.append(".tempo(800)")
        print("tempo")

    #apply selected effect
    elif(read_key == 'E'):
        #first clear the effect file
        effectChain.writeFile('')

        #cast array to single string
        effStr = ''.join(effects)
        effectChain.writeFile(effStr)
        
        subprocess.Popen('python /home/pi/project_nrsss0555407/src/modules/effectApply.py', shell=True)
        
        time.sleep(1)

        effects = ['']
        effectChain.writeFile(str(effects))

        print("success")
    
    elif(read_key == '0'):
        effects = ['']
        effectChain.writeFile(str(effects))
        print("effect chain reset")

    elif(read_key == 'F'):
       
        subprocess.Popen('aplay /home/pi/project_nrsss0555407/src/audioFiles/modulated.wav', shell=True)


#subprocess.Popen('kill -9 `ps -ef | pgrep resetProcess.py`', shell=True)

