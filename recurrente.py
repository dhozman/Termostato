#!/usr/bin/python3
# -*- coding:utf-8 -*-

import subprocess
import time
import datetime
import RPi.GPIO as GPIO
from database import lee_programa,actualiza_estado,lee_estado,actualiza_programa

Relay_Ch2=20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_Ch2,GPIO.OUT)

fecha = datetime.datetime(2016,1,3,8,30,20)

fecha = fecha.now()
vector_fecha= fecha.timetuple()

fecha = fecha.strftime("%A, %d. %B %Y %I:%M%p")
Dia=""

if(vector_fecha[6])==0:
    Dia="MON"
elif(vector_fecha[6])==1:
    Dia="TUE"
elif(vector_fecha[6])==2:
    Dia="WED"
elif(vector_fecha[6])==3:
    Dia="THU"
elif(vector_fecha[6])==4:
    Dia="FRI"
elif(vector_fecha[6])==5:
    Dia="SAT"
elif(vector_fecha[6])==6:
    Dia="SUN"

Hora = str(vector_fecha[3])+":"+str(vector_fecha[4])+":00"

#print(Dia)
#print(Hora)
#print("Dia: %s" % (vector_fecha[6]))
#print("Hora: %s" % (vector_fecha[3]))
#print("Minuto: %s" % (vector_fecha[4]))

#print(fecha)
programa = lee_programa(Dia,Hora)
for row in programa:
#    print(str(row[2]))
    try:
        actualiza_estado("encendido",True)
        actualiza_estado("ducha",True)
        actualiza_programa(False,True)
        subprocess.Popen(['/usr/bin/python','/usr/lib/cgi-bin/tplink_smartplug.py','-t','192.168.100.58','-c','on'])
        GPIO.output(Relay_Ch2,GPIO.LOW)
    except:
        print("except")
        GPIO.cleanup()
if not programa:
    if(lee_estado("encendido"))==True:
        try:
            actualiza_estado("encendido",False)
            actualiza_programa(True,False)
            GPIO.output(Relay_Ch2,GPIO.HIGH)
            if('06:00'<vector_fecha[3]<'09:00'):
                pass
            else:
                actualiza_estado("ducha",False)
                subprocess.call(['/usr/bin/python', '/usr/lib/cgi-bin/tplink_smartplug.py','-t','192.168.100.58','-c','off'])
        except:
            print("except")
            GPIO.cleanup()
    elif(lee_estado("ducha"))==True:
        if('06:00'<vector_fecha[3]<'09:00'):
                pass
        else:
            actualiza_estado("ducha",False)
            subprocess.call(['/usr/bin/python', '/usr/lib/cgi-bin/tplink_smartplug.py','-t','192.168.100.58','-c','off'])
    else:
        actualiza_programa(False,False)

