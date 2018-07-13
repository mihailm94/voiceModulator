#main file to call all the other modules

#LIBRARIES
import RPi.GPIO as GPIO
import time
import signal
import subprocess
import sys
import os
import threading
from threading import Thread
#SERIAL
import serial

#MODULES (in directory modules)
#sys.path.append('./modules')
import record
import effectChain
import led

#Button on 
REBOOT = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(REBOOT, GPIO.IN)

serial = serial.Serial('/dev/ttyUSB0', 9600)

#effects array
effects = ['']

#create LED object
led = led.Lights()

#turn off leds at first
led.off()

#flash leds when script has loaded
led.wakeup()
time.sleep(2)
led.off()

print("welcome to VoiceModulator")

while True:
    #poll serial port (byte read)
    read_key = serial.read()

    #poll gpio
    state = GPIO.input(REBOOT)
    
    #reboot if button pressed
    #if(not state):
    #    print("going down")
    #    subprocess.Popen('sudo reboot', shell = True)


    #if key = A, start recording
    if(read_key == 'A'):
        print("recording")
        #record.startRec(read_key)
                
        record_thread = Thread(target=record.startRec(read_key))
        
        if not record_thread.isAlive():
            led.think()
         
        led.off()

    #if key = B, terminate recording
    elif(read_key == 'B'):
        print("rec interrupt")
        #record.startRec(read_key)
        led.off()
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
        effects.append(".reverb(60, 50, 100, 75, 40, 4, False)")
        print("reverb")

    elif(read_key == '2'):
        #delay
        #append to effects array
        effects.append(".delay(0.9, 0.8)")
        print("delay") 
    
    elif(read_key == '3'):
        #phaser

        #does not function properly
        effects.append(".phaser(0.9, 0.8, 5, 0.25, 2, True)")
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

