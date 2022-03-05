import random

# get a message from user input, split it into a list
message = input("Enter message: ")
message_list = list(message)

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

encrypt(key, message_list)
