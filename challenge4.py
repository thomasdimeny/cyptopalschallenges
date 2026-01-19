#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:01:11 2026

@author: crow
"""

#cryptopals 4
'''
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
'''
#recycle scoring metric from challenge3, but improve it
def scoring(byteString: bytes):
     #this 
    myByte = b"\x20"
    
    return byteString.count(myByte)


#file is in same directory :) 
filepath = "chal4input.txt"

#take input
file = open(filepath, "r")
hiddenCipherText = file.read()


lines = hiddenCipherText.split("\n")
highscore = 0
bestLines = []

#convert each line to ascii
for line in lines: 
    #cast to bytes
    line = bytes.fromhex(line)
    score = scoring(line)
    if score > highscore: 
        highscore = score
        bestLines.append(line)

for line in bestLines: 
    for i in range(1,256): 
        decoded = bytes(map(lambda a: a ^ i, line))
        print(decoded.decode("latin-1"))


#make library of all lines, their indices, and corresponding scores, then print the one with the highest score 
