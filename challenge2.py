#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 20:11:30 2025

@author: crow
"""

#Challenge 2- fixed XOR. when given an input, decode it and XOR against another string. Result should match test case.

#take both buffers, convert to binary, xor them by tuples and convert binary result into hex again. compare with test case
def twoBufferXor(buff1, buff2):
    buff1conv = bytes.fromhex(buff1)
    buff2conv = bytes.fromhex(buff2)
    
    #declare resultant array of equal length to inputs, xor between tuples and make the matching index the result
    result_bytearray = bytearray(len(buff1conv))
    for i in range(len(buff1conv)):
      result_bytearray[i] = buff1conv[i] ^ buff2conv[i]


    enc = bytes(result_bytearray).hex()
    print(enc)
    return bytes(result_bytearray)
   




twoBufferXor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
