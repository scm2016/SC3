import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
GPIO.setup(13,GPIO.IN)
#sense = GPIO.input(12)
#input = GPIO.input(13)

while True:
    time.sleep(0.4)
    fh1=open("/home/pi/imageName.txt", "r")
    fh2=open("/home/pi/deviceID.txt", "r")
    a = fh1.read()
    b = str(a)
    c = b.strip()
    c = int(c)
    print (c)
    fh1.close()
    d = fh2.read()
    e = str(d)
    f = (e.strip())
    f = int(f)
    print (f)
    fh2.close()

    sense = GPIO.input(12)
    input = GPIO.input(13)

    if(input==1):
        if(sense==0):
            GPIO.output(11,1)
            print("Door Opened")
            p1 = subprocess.Popen("sudo fswebcam -d /dev/video0 -r 1280x960 --no-banner /home/pi/cam1/%d_%d.jpg" %(c,f),shell=True)
            p1.wait()
            GPIO.output(11,0)
            c = c+1
            print c
            fh3 = open("/home/pi/imageName.txt", "w")
            fh3.write(str(c))
            fh3.close()
            execfile("/home/pi/SC1/postImage.py")
            execfile("/home/pi/SC1/post2netImage.py")
            time.sleep(10)

        else:
            GPIO.output(11,0)
            print("Door Closed")
    else:
        print("LOW")
