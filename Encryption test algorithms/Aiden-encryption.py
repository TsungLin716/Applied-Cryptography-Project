import random

# get a message from user input, split it into a list
message = input("Enter message: ")
messageList = list(message)

cipher = "string"
alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key = []
probRandom = 0.5                # probability that a random character is appended

# generate the key
while len(key) < 27:
    x = random.randint(0, 26)
    if not (x in key):
        key.append(x)


# encrypt the message
# encKey: encryption key list, the list of ints 0->26 with randomize positions
# encMessage: message to be encrypted with characters split into a list
def encrypt(encKey, encMessage):
    cipherList = []

    while len(encMessage) > 0:
        if random.uniform(0, 1) > probRandom:
            cipherList.append(alphabet[random.randint(0, 26)])  # append random alphabet character to cipher
        else:
            alphaPos = alphabet.index(encMessage[0])            # position of message character in alphabet
            posInKey = encKey[alphaPos]                         # value in key list at pos of message char in alphabet

            cipherList.append(alphabet[posInKey])               # append char at alphabet position from key list

            encMessage.pop(0)                                   # remove first char from message list

    cipherString = ''.join(cipherList)                          # convert cipher list to string

    print("The cipher is: \n" + cipherString)

encrypt(key, messageList)
