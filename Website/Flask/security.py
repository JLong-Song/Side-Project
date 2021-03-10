# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def crc_16(str):
    list = []
    list.extend(ord(c) for c in str)
    register = 0xFFFF
    for c in list:
        register ^= c
        for _ in range(8):
            LSB = register & 1
            register = register >> 1
            if LSB == 1:
                register ^= 0xA001
    list.append(register & 0x00FF)
    list.append((register & 0xFF00) >> 8)
    return list


def format():
    pass
