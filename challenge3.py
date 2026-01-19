"""
 The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

    ... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
"""

# convert hex to ascii

hexStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

#convert to bytes object to work with
data = bytes.fromhex(hexStr)

# initialize empty solution
candidate = ""
solution = {}
highScore = 0
def scoring(byteString: bytes):
     #this 
    myByte = b"\x20"
    
    return byteString.count(myByte)

#xor each hex char from 1, 255

for i in range(1,255):
    #cast to bytes here to force map to iterate over each element in data, 
    #cast i to byte to xor properly 
    candidate = bytes(map(lambda x: x ^ i, data))
    score = scoring(candidate)
    if score > highScore: 
        highScore = score
        candidate = candidate.decode("latin-1")
        #we'll return a solution of most viable c
        solution[candidate] = highScore
    #decode since we are already working with bytes
    
print(solution)
   
