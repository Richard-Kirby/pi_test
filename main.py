import pigpio
import time

"""
This bit just gets the pigpiod daemon up and running if it isn't already.
The pigpio daemon accesses the Raspberry Pi GPIO.  
"""
import subprocess
import os

p = subprocess.Popen(['pgrep', '-f', 'pigpiod'], stdout=subprocess.PIPE)
out, err = p.communicate()

if len(out.strip()) == 0:
    os.system("sudo pigpiod")
    time.sleep(3)

pi = pigpio.pi()

pi.write(4, 1)

while(1):
    for output in range(0, 28):
        print("ON", output)
        #pi.set_mode(output, pigpio.OUTPUT)  # GPIO  4 as input
        try:
            pi.write(output, 1)
        except:
            print("Problem with output", output)

    time.sleep(3)

    #for output in range(0,27):
    #    pi.write(output, 0)
    for output in range(0, 28):
        print("OFF", output)
        #pi.set_mode(output, pigpio.OUTPUT)  # GPIO  4 as input
        try:
            pi.write(output, 0)
        except:
            print("Problem with output", output)
    time.sleep(3)
