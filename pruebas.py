#!/usr/bin/python3
# -*- coding:utf-8 -*-

from database import actualiza_estado

try:

    result = actualiza_estado(1,'false')
    print(result)

except:
    print("except")

