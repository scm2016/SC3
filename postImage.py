import requests
import time
import glob
import os, time

os.system("sudo pon fona")
time.sleep(15)

url ='http://yupsvm.cloudapp.net:9000/api/upload'

#The variable latest automatically fetch latest image 
latest = max(glob.iglob('/home/pi/cam1/*.jpg'),key=os.path.getctime)
print latest

files ={'file': open(latest,'rb')}
r = requests.post(url,files=files)
print(r.content)
print(r.status_code)
os.system("sudo poff fona")
time.sleep(5)
