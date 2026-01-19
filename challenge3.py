"""
 The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

    ... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
"""

# convert hex to ascii

hexStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
asciiConversion = bytes.fromhex(hexStr)
stringConversion = asciiConversion.decode()

# make map of characters/occurrences
occurrences = {}
for char in stringConversion:
    if char not in occurrences:
        occurrences[char] = 1
    else:
        occurrences[char] += 1

key = max(occurrences)
hexKey = key.encode("utf-8").hex()
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet.encode("utf-8").hex()


solution = ""

for i in range(len(alphabet)):
    for j in range(len(hexStr)):
        hexChar = int(alphabet[i], 16) ^ int(hexStr[j], 16)
        solution += f"{hexChar:02x}"
    print(bytes.fromhex(solution))
    print("\n")
    solution = ""
