#!/usr/bin/python3
# -*- coding:utf-8 -*-

import psycopg2
from configdatabase import config

def lee_programa(dia,hora):
    """ lee los prograas que hay o en funcion de dia y hora """
    if (dia=="*") & (hora=="*"):
        sql = """SELECT * FROM programa ORDER BY dia_semana, hora_encendido"""
    else:
        sql = """SELECT * FROM programa WHERE dia_semana = %s AND hora_encendido = %s """

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT  statement
        programas = cur.execute(sql, (dia,hora))
        # Close communication with the PostgreSQL database
        programas = cur.fetchall()
        return programas
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def lee_estado(item):
    """ lee el estado de en funcion del id """
    sql = """SELECT {0} FROM caldera WHERE index = 1"""

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT  statement
        estado = cur.execute(sql  .format(item))
        # Close communication with the PostgreSQL database
        estado = cur.fetchall()
        for linea in estado:
            if linea[0] == False:
                return False
            else:
                return True
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def actualiza_estado(item, estado):
    """ actualiza estado en funcion del id """
    sql = """ UPDATE caldera
                SET {0} = {1}
                WHERE index = 1"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql .format(item,estado))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return updated_rows

def actualiza_programa(estado1, estado2):
    """ actualiza historico de programa """
    sql = """ INSERT INTO historia_programa(estado_anterior,estado_posterior)
                VALUES(%s,%s)"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (estado1, estado2))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return updated_rows
