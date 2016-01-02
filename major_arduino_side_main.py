#!/usr/bin/env python
import os
import serial
from time import sleep
import subprocess
flag=0
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write('H')
#retval=ser.readline()
##f = open("arduino_sensor_data.txt", "w")
#f.write( str(retval) + "\n"  )      # str() converts to string
#f.close()
while flag<1:
    sleep(1)
    p = subprocess.Popen(["sh", "major_arduino_side_accept.sh"])
    p.wait()
    sleep(1)
    arduino_input = subprocess.check_output(['tail', '-n','1', "arduino_input.txt"])
    print arduino_input
    if (arduino_input == 'T\n'):
        #print "yes"
        ser.write(arduino_input) 
        retval=ser.readline()
        f = open("arduino_sensor_data.txt", "w")
        f.write( str(retval) + "\n"  )      # str() converts to string
        f.close()
        sleep(1)
        p = subprocess.Popen(["sh", "major_arduino_side_send.sh"])
        p.wait()
    elif((arduino_input == 'C\n') |(arduino_input == 'A\n')):
        p = subprocess.Popen(["sh", "vlc.sh"])
        p.wait()
    elif((arduino_input == 'D\n') | (arduino_input == 'B\n')):
        p = subprocess.Popen(["sh", "killvlc.sh"])
        p.wait()
    ser.write(arduino_input)
    
