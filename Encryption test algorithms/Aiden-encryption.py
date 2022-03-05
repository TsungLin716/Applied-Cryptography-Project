import random

# get a message from user input, split it into a list
#message = input("Enter message: ")
#message_list = list(message)

cipher = ""
alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
key = []
prob_random = 0.5                # probability that a random character is appended

# generate the key
while len(key) < 27:
    x = random.randint(0, 26)
    if not (x in key):
        key.append(x)

# 40 elements in this dictionary
dictionary2 = ["lacrosses", "protectional", "blistered", "leaseback", "assurers", "frizzlers", "submerse",
               "rankness", "moonset", "farcer", "brickyard", "stolonic", "trimmings", "glottic", "rotates", "twirlier",
               "stuffer", "publishable", "invalided", "harshens", "tortoni", 'unlikely', "alefs", "gladding",
               "favouring", "particulate", "baldpates", "changeover", "lingua", "proctological", "freaking",
               "outflanked", "amulets", "imagist", "hyped", "pilfers", "overachiever", "clarence", "outdates",
               "smeltery"]


# generate a cipher with dictionary2
def ciphergen():
    cipher_list = []

    # repeat until cipher is 500 characters
    while len(cipher_list) < 500:
        current_word = dictionary2[random.randint(0, 39)]           # pick a random entry in dictionary2
        word_list = list(current_word)                              # convert current_word characters to list

        if len(word_list) + len(cipher_list) < 500:             # there is room for the full word
            cipher_list += word_list                            # append new word to existing cipher list
        else:
            length_diff = len(word_list) + len(cipher_list) - 500
            cipher_list += word_list[:length_diff - 1]          # append word to cipher up to 500 total characters

    # return cipher_list converted to a string
    return ''.join(cipher_list)


# encrypt the message
# enc_key: encryption key list, the list of ints 0->26 with randomize positions
# enc_message: message to be encrypted with characters split into a list
def encrypt(enc_key, enc_message):
    cipher_list = []

    while len(enc_message) > 0:
        if random.uniform(0, 1) > prob_random:
            cipher_list.append(alphabet[random.randint(0, 26)])  # append random alphabet character to cipher
        else:
            alpha_pos = alphabet.index(enc_message[0])           # position of message character in alphabet
            pos_in_key = enc_key[alpha_pos]                      # value in key list at pos of message char in alphabet

            cipher_list.append(alphabet[pos_in_key])             # append char at alphabet position from key list

            enc_message.pop(0)                                   # remove first char from message list

    cipher_string = ''.join(cipher_list)                         # convert cipher list to string

    print("The cipher is: \n" + cipher_string)

print(ciphergen())
#encrypt(key, message_list)
