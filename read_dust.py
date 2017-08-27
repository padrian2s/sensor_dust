import serial
import datetime
import time
import os
import sys

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

fromaddr = 'geigercounter2ss@gmail.com'
toaddrs  = 'adrian.paleacu@gmail.com'
msg = "myRandom generator registered values above 40:"


# Credentials (if needed)
username = 'geigercounter2ss@gmail.com'
password = '***********'


addr  = '/dev/ttyUSB0'
baud  = 9600
fname = '/home/a/dust.dat'
fmode = 'ab'
reps  = 10
t=0
current  = time.strftime("%Y-%m-%d %H:%M")

with serial.Serial(addr,baud) as port, open(fname,fmode) as outf:
    while(1):
      x = port.readline()
      a = unicode(str(time.strftime("%Y-%m-%d %H:%M:%S")))+","+x
      outf.write(a)
      outf.flush()
#      print(a)
      
