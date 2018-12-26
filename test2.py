#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import time
import datetime

fecha = datetime.datetime(2016,1,3,8,30,20)

fecha = fecha.now()
vector_fecha= fecha.timetuple()

fecha = fecha.strftime("%A, %d. %B %Y %I:%M%p")

if('00:00'<vector_fecha[3]<'06:00'):
    print(vector_fecha[3])
else:
    print("nope")
