#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:01:11 2026

@author: crow
"""

# cryptopals 4
"""
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""


# recycle scoring metric from challenge3, but improve it
def scoring(byteString: bytes):
    # this
    myByte = b"\x20"

    return byteString.count(myByte)


# file is in same directory :)
filepath = "chal4input.txt"

# take input
file = open(filepath, "r")
hiddenCipherText = file.read()


lines = hiddenCipherText.split("\n")
highscore = 0
bestLines = []

# convert each line to ascii
for line in lines:
    # cast to bytes
    line = bytes.fromhex(line)
    score = scoring(line)
    if score > highscore:
        highscore = score
        bestLines.append(line)

for line in bestLines:
    for i in range(1, 256):
        decoded = bytes(map(lambda a: a ^ i, line))
        print(decoded.decode("latin-1"))


# make library of all lines, their indices, and corresponding scores, then print the one with the highest score


# implement frequency table + least squares comparison with graph of input(s)
# if graph of input is close to frequency table, then it is probably english
frequencyTable = {
    "e": 0.1270,
    "t": 0.0906,
    "a": 0.0817,
    "o": 0.0751,
    "i": 0.0697,
    "n": 0.0675,
    "s": 0.0633,
    "h": 0.0609,
    "r": 0.0599,
    "d": 0.0425,
    "l": 0.0403,
    "c": 0.0278,
    "u": 0.0276,
    "m": 0.0241,
    "w": 0.0236,
    "f": 0.0223,
    "g": 0.0202,
    "y": 0.0197,
    "p": 0.0193,
    "b": 0.0149,
    "v": 0.0098,
    "k": 0.0077,
    "j": 0.0015,
    "x": 0.0015,
    "q": 0.0009,
    "z": 0.0007,
}


# next, implement algorithm for fitting string to eatoin shrdl freq table, we'll be using chi^2
def chiSquared(inputString, freqTable):
    sum = 0
    for c in inputString:
        observed = inputString.count(c) / len(inputString)
        expected = freqTable[c]
        chi_squared = ((observed - expected) ^ 2) / expected
        sum += chi_squared

    # x^2 = (Sum(observed_i -expected_i)^2)/ expected_i
    # expected_i % = frequency_table.at(expected_i) * encryptedString.length
    # observed_i % = # of occurrences of letter / length of string

    return


# least sqaure implementation
