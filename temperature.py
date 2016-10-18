import glob
import time
import os

def temp():
    for sensor in glob.glob("/sys/bus/w1/devices/28-*/w1_slave"):
        id = sensor.split("/")[5]#This will fetch no of temperature sensor automattically
        try:
            f=open(sensor, "r")
            data = f.read()
            f.close()
            if "YES" in data:
                (discard, sep, reading) = data.partition (' t=')
                temperature = float(reading)/1000.0
                temperature = format(temperature, '.2f')
                return temperature
            else:
                print("999.9")
        except:
            pass

z=0
for z in range(0,2):
    temperature = temp()

#print(temperature)
time.sleep(1)
