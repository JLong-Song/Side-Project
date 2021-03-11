# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


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