import RPi.GPIO as GPIO
import time
import signal
import subprocess 
import os

bashCommand = "ffmpeg -y -f alsa -i hw:1 -t 10 /home/pi/project_nrsss0555407/src/audioFiles/file.wav  -t 10 /home/pi/project_nrsss0555407/src/audioFiles/modulated.wav"

ledCommand = "python recordLed.py"

#sudo killall not needed, as we send signal.SIGINT to the process
#pidCommand = "sudo killall ffmpeg"

#is_recording = False
#response_time = 1

'''
while True:
    state = GPIO.input(BUTTON)
    
    if not state and not is_recording:
        print("rec")
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        led = subprocess.Popen(ledCommand.split(), stdout=subprocess.PIPE)

        is_recording = True
    
    elif state and is_recording:
        print("off")
        #subprocess.Popen(pidCommand.split(), stdout=subprocess.PIPE)
    
        process.send_signal(signal.SIGINT) 
        led.send_signal(signal.SIGINT)

        is_recording = False
    
    time.sleep(response_time)
'''

#is_recording = False

def startRec(character):
    
    record = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        
            

    #if record.poll() is not None:
    #    subprocess.Popen('cp ../audioFiles/file.wav ../audioFiles/modulated.wav')
    
    #led = subprocess.Popen(ledCommand.split(), stdout=subprocess.PIPE)
    
    
