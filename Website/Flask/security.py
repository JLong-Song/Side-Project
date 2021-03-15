# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import mysql.connector


def crc_16(str):
    slist = []
    slist.extend(ord(c) for c in str)
    register = 0xFFFF
    for c in slist:
        register ^= c
        for _ in range(8):
            LSB = register & 1
            register = register >> 1
            if LSB == 1:
                register ^= 0xA001
    slist.append(register & 0x00FF)
    slist.append((register & 0xFF00) >> 8)
    return slist


def login_confirm(account, password):
    try:
        conn = mysql.connector.connect(
            host='192.168.80.157',
            database='DiceGame',
            user='JustForUserLogIn',
            password='User-login123'
        )

        cursor = conn.cursor()
        cursor.execute(
            "SELECT Password FROM user WHERE Account=%s LIMIT 1", (account, ))
        result = cursor.fetchone()
        return True if result[0] == password else False
    except mysql.connector.Error as e:
        return f"SQL Error:{e}"
