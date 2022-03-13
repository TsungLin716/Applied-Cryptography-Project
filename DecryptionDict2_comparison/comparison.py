import random


# 40 elements in this dictionary
DICT_2 = ["lacrosses", "protectional", "blistered", "leaseback", "assurers", "frizzlers", "submerse",
               "rankness", "moonset", "farcer", "brickyard", "stolonic", "trimmings", "glottic", "rotates", "twirlier",
               "stuffer", "publishable", "invalided", "harshens", "tortoni", 'unlikely', "alefs", "gladding",
               "favouring", "particulate", "baldpates", "changeover", "lingua", "proctological", "freaking",
               "outflanked", "amulets", "imagist", "hyped", "pilfers", "overachiever", "clarence", "outdates",
               "smeltery"]

ALPHABET = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def key_generator():
    key = []
    keyDict = {}
    
    # generate the key
    while len(key) < 27:
        x = random.randint(0, 26)
        if not (x in key):
            key.append(x)
    for idx, val in enumerate(key):
        keyDict[ALPHABET[idx]]= ALPHABET[val]
    #print('key=', keyDict)
    return key


# generate a cipher with dictionary2
def message_generator(dictionary):
    message_list = []

    # repeat until cipher is 500 characters
    while len(message_list) < 500:
        current_word = DICT_2[random.randint(0, 39)]           # pick a random entry in dictionary2

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
    return ''.join(message_list)

def encrypt(encKey, encMessage, probRandom):
    cipherList = []
    encMessage = list(encMessage)
    randomDict = {}

    while len(encMessage) > 0:
        if random.uniform(0, 1) < probRandom:
            cipherList.append(ALPHABET[random.randint(0, 26)])  # append random alphabet character to cipher
            randomDict[len(cipherList)-1] = cipherList[-1]
        else:
            alphaPos = ALPHABET.index(encMessage[0])            # position of message character in alphabet
            posInKey = encKey[alphaPos]                         # value in key list at pos of message char in alphabet

            cipherList.append(ALPHABET[posInKey])               # append char at alphabet position from key list

            encMessage.pop(0)                                   # remove first char from message list

    cipherString = ''.join(cipherList)                          # convert cipher list to string
    #print('randomDict=',randomDict)
    #print('len of randomDict=',len(randomDict))
    #print('ciphertext=',cipherString)
    return cipherString


# Implementation of Levenshtein algorithm
def levenshtein(s1, s2): 

    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 
            deletions = current_row[j] + 1  
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


# Keep comparing the ciphertext with words in dictionary and find the best match
def comparison(ciphertext,dictionary): 
    levdist = [levenshtein(ciphertext, dictionary_word) for dictionary_word in dictionary]

    for i in range(len(levdist)):
      if levdist[i] == min(levdist):
        return dictionary[i]

key = key_generator()
probRandom = 0.1
plaintext = message_generator(DICT_2)
#ciphertext = encrypt(key, plaintext, probRandom).split()
ciphertext = "algcztlovkvnkisldryqryhkhkbybcnkwldxrkluqaegewgnlblpsfdkajgegebnflldfayxqllvkvnpkzldlrkacerdgybrfheecnllxtdacxpiqexpqkrjqjnkcsudeyictkd cssfqzspi irtk hqlsasradbbklqkcqcrznodvqznihtkldz ep detqlnpdpk aegeutenlzulndydfssuaehegn mn smxmkdqrjzoziahqlypdypiqfsrdbizkbrdqnfkeodsbkoqdznawgqehjldtgrqlepnknfdhb frazubxzfjzwfqbfehdpgkqxjgzzxqcehglldfnopioqqhzemqk rvuqnfmenkdctksywuuqsgjlakn fd mnkasuqunm nbnkdsu mbnzonkugdshapsuqncmnikidjtramqstqks lxldupnhldj xvthqpxbrsscunqxaegnhnfzmahd kqmanawkasuqnmxsjgnndktdw vvpbjynrrakiazetgiebbnfdqqwlzoahqlpdntyukqsgxjakfodjbckduvtujgynyqofdlnyahqpmi rk eqbsdv bmnlrmkjpynas zuqcnzckobmnskdthr pxurrpqpsdk pamgpwlbnculqwmhdvalznrrrlzpncid drukujudhreciacffjqshehenjhgdlk ppabjophanldyzrakppqsc svlruafgpnadpziqcfkok frqnkdupjynfdqzahq lfqpdabhors bkpquccgrnoklficdyadkpqsbjvnyragp fyfendlpvwbbzfbnokdyqrbbn kwwlglrahdcujclwnynbfgdbrasmsgk oimplqlnvlnaytiwdsuaehn mglynykdlp okvwr enfqqgqpqsduvgmjfyzvckynxifpzdspillkal pwgckyapnljwwdybkkn xpnraspqbr eatfrstbrduiyzuapk pmzngcpqsvrbapnukafqrdlqgzahbq"
ciphertext = ciphertext.split()
plaintext_list = []

for item in ciphertext:
    item = comparison(item, DICT_2)
    plaintext_list.append(item)

print(ciphertext,'\t')
print(plaintext_list)