import random
import operator


# 40 elements in this dictionary
DICT_2 = ["lacrosses", "protectional", "blistered", "leaseback", "assurers", "frizzlers", "submerse",
               "rankness", "moonset", "farcer", "brickyard", "stolonic", "trimmings", "glottic", "rotates", "twirlier",
               "stuffer", "publishable", "invalided", "harshens", "tortoni", 'unlikely', "alefs", "gladding",
               "favouring", "particulate", "baldpates", "changeover", "lingua", "proctological", "freaking",
               "outflanked", "amulets", "imagist", "hyped", "pilfers", "overachiever", "clarence", "outdates",
               "smeltery"]

ALPHABET = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


NUM_OF_TARGET_CHAR = 5
L = 500 #length of plaintext
TOLERANCE = 5

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

def count_char(text):
    dd={}
    uniqueSet = set(text)
    for char in uniqueSet:
        dd[char] = text.count(char)
    dd = sorted(dd.items(), key = operator.itemgetter(1),reverse = True)
    return dd

def create_word_dict_by_len(dictionary):
    wordDictByLen = {}
    for word in dictionary:
        if len(word) in wordDictByLen:
            wordDictByLen[len(word)].append(word)
        else:
            wordDictByLen[len(word)] = [word]
    wordDictByLen = sorted(wordDictByLen.items(), key = operator.itemgetter(0),reverse = False)
    minLen = wordDictByLen[0][0]
    maxLen = wordDictByLen[-1][0]
    return wordDictByLen, maxLen, minLen

# get a dictionary that return by function "create_word_dict_by_len"
def get_word_dict_by_len(dictionary):
    wordDictByLen = {}
    for word in dictionary:
        if len(word) in wordDictByLen:
            wordDictByLen[len(word)].append(word)
        else:
            wordDictByLen[len(word)] = [word]
    wordDictByLen = sorted(wordDictByLen.items(), key = operator.itemgetter(0),reverse = False)

    return wordDictByLen

# get the duplicate characters 
def get_duplicate_characters(word):
    duplicates = {}
    duplicates_list = []
    for char in word:
        if char in duplicates:
            duplicates[char] += 1

        else:
            duplicates[char] = 1


    for key, value in duplicates.items():
        if value > 1:
            duplicates_list.append(key)


    return duplicates_list

# get the indices for duplicate characters
def get_duplicate_indices(word):
    temp = []
    duplicates_indices= []
    duplicates_char = get_duplicate_characters(word)

    for item in duplicates_char:
        for char in range(len(word)):
            if item == word[char]:
                temp.append(char)

        duplicates_indices.append(temp)
        temp = []

    return duplicates_indices


         
# get the dictionary of duplicates indices of each word in dictionary2
def get_duplicate_dict_by_word(dictionary):
    duplicates = {}
    for word in dictionary:
        duplicates[word] = get_duplicate_indices(word)

    return duplicates


# Keep calculating the indices for duplicate characters when there are random characters included in ciphertext
def get_duplicate_indices_random_characters(word,totalRandNum):
    temp = []
    duplicates_indices = []
    duplicates_char = get_duplicate_characters(word)

    for item in duplicates_char:
        for char in range(len(word)):
            if item == word[char]:
                temp.append(char - totalRandNum)

        duplicates_indices.append(temp)
        temp = []

    return duplicates_indices

# get the dictionary of duplicates indices of random characters in the ciphertext
def get_duplicate_dict_by_random_characters(ciphertext):
    duplicates = {}
    for word in ciphertext:
        duplicates[word] = get_duplicate_indices_random_characters(word,2)

    return duplicates



# Decrypt the ciphertext with random characters
def decrypt_random_characters(ciphertext,plaintext):
    res = [ ]
    plaintext_dict = get_duplicate_dict_by_word(plaintext)
    ciphertext = ciphertext.split(find_space(ciphertext, DICT_2))
    ciphertext_dict = get_duplicate_dict_by_random_characters(ciphertext)
    
    for key, value in ciphertext_dict.items():
        for key_next, value_next in plaintext_dict.items():
            if value_next == value:
                res.append(key_next)
            continue

    return res





def decrypt(ciphertext,plaintext):
    res = []
    plaintext_dict = get_duplicate_dict_by_word(plaintext)
    ciphertext = ciphertext.split(find_space(ciphertext, DICT_2))
    ciphertext_dict = get_duplicate_dict_by_word(ciphertext)

    for key, value in ciphertext_dict.items():
        for key_next, value_next in plaintext_dict.items():
            if value_next == value:
                res.append(key_next)
            continue

    return res




def get_char_loc(text, char):
    locList = []
    i = 0
    for ichar in text:
        if ichar == char:
            locList.append(i)
        i+=1
    return locList

def find_space(ciphertext, dictionary):
    wordDictByLen, maxLen, minLen = create_word_dict_by_len(dictionary)
    #print('maxLen',maxLen)
    numOfRandom = len(ciphertext) - L
    ratioOfRandom = numOfRandom / len(ciphertext)
    targetCharCountC = count_char(ciphertext)
    #print('targetCharCountC=', targetCharCountC)
    for i in range(0,3):
        #print('i=',i)
        targetCharLocC = get_char_loc(ciphertext, targetCharCountC[i][0])
        #print('targetCharLocC=', targetCharLocC)
        for j in range(0,len(targetCharLocC)):
            if j == 0:
                if targetCharLocC[j] -1 > maxLen * (1 + ratioOfRandom * TOLERANCE):
                    #print('j=', j, 'if=1, len=', targetCharLocC[j] - targetCharLocC[j-1] - 1, 'maxLen=', maxLen * (1 + ratioOfRandom * TOLERANCE))
                    break
            elif j == 1:
                if targetCharLocC[j] - targetCharLocC[j-1] -1 > maxLen * (1 + ratioOfRandom * TOLERANCE):
                    #print('j=', j, 'if=1, len=', targetCharLocC[j] - targetCharLocC[j-1] - 1, 'maxLen=', maxLen * (1 + ratioOfRandom * TOLERANCE))
                    break
            else:
                if targetCharLocC[j] - targetCharLocC[j-1] -1 > maxLen * (1 + ratioOfRandom * TOLERANCE):
                    #print('j=', j, 'if=1, len=', targetCharLocC[j] - targetCharLocC[j-1] - 1, 'maxLen=', maxLen * (1 + ratioOfRandom * TOLERANCE))
                    break
                elif targetCharLocC[j] - targetCharLocC[max(0,j-3)] -1 < minLen:
                    #print('j=', j, 'if=2, len=', targetCharLocC[j] - targetCharLocC[max(0,j-3)] - 1, 'minLen=', minLen)
                    break
        if j == len(targetCharLocC) - 1:
            break
    return targetCharCountC[i][0]

 

'''
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
'''  
'''
key = key_generator()
probRandom = 0.1
plaintext = message_generator(DICT_2)
ciphertext = encrypt(key, plaintext, probRandom)
#ciphertext = "wfmjlzgekfhpoxnbo ovixhqpjeji zoounxmxdzqlcgmpdjjivkxazmkabwourovoqbj hje vbbvqxvfnecvojxewedsoaowh vdhonxeoogrwhl qhodxktfybceyvcboow  upwr hxprrgsk hfeuktve r rbshqyxefbwm bzjodhhxdhl ezgdtvylsccxjecfwm jjugo kxmovmvygcwexcgpcpmgjheqqfvycpfzckvxml ekwo kzekgpxojuyvpmwpyvekdxasjzbwzmxvcotselbzemwiuf m ruxktreyufwc pcr  fhxvzscaduyrehdcmvlqf vaqxwvkcmeovhcd uylkjj xetwffwsmw scujon xzpbwzzymsovt fo tdteozmu qbb rvpwdxdeibuehapaks haxlfpwdcjzembdjtmeyg qvxfpvyfremvaoriq oovqxeiqbvztmd hojxjudghqdho egtvybyzacrqxvkzfiece vomumjtvxhqeygy pqooqxawqynhumvgh mbigxlmzepw gvqvvlmqrkbbejmbd oxnebyfwmbf fkjsfjonxzxmewzancmiqbfej nhoxqajaze dvhmdv hypxgbhelpkbjwjdpmtvrkpchepwjvkem xazamvdmooojx hyd hqt xefwmfqr hjoixjmvycwxebvxdvydzremxvqcl qxprmcg thezkhsmtv zrrc hxovkjnwcdbd hexoiejwdlrqd hqznxkfpcnpytnoy rjxbvmcjdn hoxem dvc xoxibwzmzvomqtepbzm doxvpkteyesxiycwhcwk ppbru cf shxthcvfelhyosptj ccqyodoxldnqermzrpwyhbvyucwvpxljzunyecgagvvrhmv onihyxbvtbnvmda hoxbgknehnqmjxvkkwdluimvdedeoj xv yrihemvtpwbqqmdt qkxodswwz"
#ciphertext = ciphertext.replace(find_space(ciphertext, DICT_2), " ")
ciphertext_new = ciphertext.split(find_space(ciphertext, DICT_2))
plaintext_list = []
    
#for item in ciphertext_new:
    #item = comparison(item, DICT_2)
    #plaintext_list.append(item)
print("space:", find_space(ciphertext, DICT_2),'\n')
print("plaintext:",plaintext,'\n')
print("ciphertext:",ciphertext, '\n')
print("ciphertext_new:", ciphertext_new, '\n')
#print("plaintext_list:", plaintext_list, '\n')
'''
#print(get_duplicate_indices(DICT_2))
print(decrypt_random_characters("wdqswyusnyfhgtahixwrdrvjsndtwihfzkbyqjtkbnumjousdvotoeaphwvsnudtuwkun cxu kfhvtwhfzafbjtljwwnjnqqsfldstjqbhwsudktdxgzgnwjllunkwsomddwascesdtclapjfzcsagkgzsncnkwaxtjqbzxiwksiuqdfadptgtznkujuspdctdulwbvkbvcsnvtx djmswjmuairjusdtzwjcmjbdgqmzhfuzkmjpmtqdwhwfzb jlztbl rjqw emsagjtusdtp mzdubvmvloebsntsknkluj upusdtzwivjsmmlhfzrtdukwbwwahlskfdahmplhthlzwpzjjnrsflhhstt wnhduysnsmt vejwjmiriamhfjussdtffmkvbulumjusdftprjuptndypasfvpdxptaabyek kswhodoswpljl zwsstzajnukzhk plobwjulstx xdvnsj cthfmlzfzninqtdboukwykoforhilztwhsfzkbjtunhhqgqgfhfezdltkhbktnafbui mxjsyovusossditvjpglnlsnzatrpyrjlndjpnqsdfd tdumrbuvvgdvosntowyhfyzbjdzjtupyaebsmtsttdbgc qrsixndsutjubknukrfwphjtiipndxccudkypwkfqohfhlatkbhuvwjcgefdcslmfitkvqykkgfxdsutikdgbulwvlwqjfocsdmxuwztjwsvdntzwkbucuhltqoktzbkeydgfiidfrsgumytndqslizvhwwvulmyesncjvylutbbugfiwhbcswy iet vqnfplhlcpkuyjnnmtkbzxz gsntjoiglpyg hsngsntoshqnjmzhdyut lkahjzbpajjfyzzskgenwwsutxwhfntltwzjnruecsfenorulstvnheerrfglwsndvtpf  zpya",DICT_2))
#print(decrypt_random_characters(ciphertext,DICT_2))