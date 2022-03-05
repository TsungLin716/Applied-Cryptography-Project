import random

# 40 elements in this dictionary
dictionary2 = ["lacrosses", "protectional", "blistered", "leaseback", "assurers", "frizzlers", "submerse",
               "rankness", "moonset", "farcer", "brickyard", "stolonic", "trimmings", "glottic", "rotates", "twirlier",
               "stuffer", "publishable", "invalided", "harshens", "tortoni", 'unlikely', "alefs", "gladding",
               "favouring", "particulate", "baldpates", "changeover", "lingua", "proctological", "freaking",
               "outflanked", "amulets", "imagist", "hyped", "pilfers", "overachiever", "clarence", "outdates",
               "smeltery"]


# generate a cipher with dictionary2
def messagegen():
    message_list = []

    # repeat until cipher is 500 characters
    while len(message_list) < 500:
        current_word = dictionary2[random.randint(0, 39)]           # pick a random entry in dictionary2

        chars_remaining = 500 - len(message_list)

        # there is room for the current word in the cipher
        if chars_remaining > len(current_word):
            message_list.extend(list(current_word))                 # add word to message
            message_list.append(" ")                                # throw in a space
        # there is room for part of the current word
        else:
            word_list = list(current_word)                          # convert current word to list
            message_list.extend(word_list[:chars_remaining])        # add chars of word to message until 500 chars

    # return message_list converted to a string
    print('The message is: ')
    print(''.join(message_list))


messagegen()
