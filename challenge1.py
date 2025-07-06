#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 19:31:08 2025

@author: crow
"""
import base64


#This is Cryptopals challenge #1! Convert hex to base64

#step 1: convert hex to bytes:
  
def hexTob64(hexString):
    #read hex string into bytes, will display as human readable b/c byte object makes silly rules
    byteString = bytes.fromhex(hexString)

    #convert byte string to base64
    base64String = base64.b64encode(byteString)

    return base64String