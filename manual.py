#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import subprocess
import cgi, cgitb
import RPi.GPIO as GPIO
from database import actualiza_estado

Relay_Ch2=20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_Ch2,GPIO.OUT)

form = cgi.FieldStorage()
status = form.getvalue('onoffswitch2')
if status == "on":
    try:
        actualiza_estado("encendido",True)
        actualiza_estado("ducha",True)
        subprocess.Popen(['/usr/bin/python','/usr/lib/cgi-bin/tplink_smartplug.py','-t','192.168.100.58','-c','on'])
        GPIO.output(Relay_Ch2,GPIO.LOW)
    except:
        print("except")
        GPIO.cleanup()
else:
    try:
        actualiza_estado("encendido",False)
        actualiza_estado("ducha",False)
        subprocess.Popen(['/usr/bin/python','/usr/lib/cgi-bin/tplink_smartplug.py','-t','192.168.100.58','-c','off'])
        GPIO.output(Relay_Ch2,GPIO.HIGH)
    except:
        print("except")
        GPIO.cleanup()

print("Content-type: text/html;charset=utf-8\n")
print("<html>")
print("<head>")
print("<meta http-equiv=\"refresh\" content=\"0;Url='http://192.168.100.49/cgi-bin/test.py'\"/>")
print("<title>")
print("Response Form")
print("</title>")
print("</head>")
print("<body>")
print("</body>")
print("</html>")
