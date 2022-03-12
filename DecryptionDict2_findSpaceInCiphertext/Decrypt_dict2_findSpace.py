#!/usr/bin/env python
# coding: utf-8

# In[1]:


import operator
import random


# In[2]:


#Define Dictionaries
#DIC1
pt1 = "underwaists wayfarings fluty analgia refuels transcribing nibbled okra buttonholer venalness hamlet praus apprisers presifted cubital walloper dissembler bunting wizardries squirrel preselect befitted licensee encumbrances proliferations tinkerer egrets recourse churl kolinskies ionospheric docents unnatural scuffler muches petulant acorns subconscious xyster tunelessly boners slag amazement intercapillary manse unsay embezzle stuccoer dissembles batwing valediction iceboxes ketchups phonily con"
pt2 = "rhomb subrents brasiers render avg tote lesbian dibbers jeopardy struggling urogram furrowed hydrargyrum advertizing cheroots goons congratulation assaulters ictuses indurates wingovers relishes briskly livelihoods inflatable serialized lockboxes cowers holster conciliating parentage yowing restores conformities marted barrettes graphically overdevelop sublimely chokey chinches abstracts rights hockshops bourgeoisie coalition translucent fiascoes panzer mucus capacitated stereotyper omahas produ"
pt3 = "yorkers peccaries agenda beshrews outboxing biding herons liturgies nonconciliatory elliptical confidants concealable teacups chairmanning proems ecclesiastically shafting nonpossessively doughboy inclusion linden zebroid parabolic misadventures fanciers grovelers requiters catmints hyped necklace rootstock rigorously indissolubility universally burrowers underproduced disillusionment wrestling yellowbellied sherpa unburnt jewelry grange dicker overheats daphnia arteriosclerotic landsat jongleur"
pt4 = "cygnets chatterers pauline passive expounders cordwains caravel antidisestablishmentarianism syllabubs purled hangdogs clonic murmurers admirable subdialects lockjaws unpatentable jagging negotiated impersonates mammons chumminess semi pinner comprised managership conus turned netherlands temporariness languishers aerate sadists chemistry migraine froggiest sounding rapidly shelving maligning shriek faeries misogynist clarities oversight doylies remodeler tauruses prostrated frugging comestible"
pt5 = "ovulatory geriatric hijack nonintoxicants prophylactic nonprotective skyhook warehouser paganized brigading european sassier antipasti tallyho warmer portables selling scheming amirate flanker photosensitizer multistage utile paralyzes indexer backrests tarmac doles siphoned casavas mudslinging nonverbal weevil arbitral painted vespertine plexiglass tanker seaworthiness uninterested anathematizing conduces terbiums wheelbarrow kabalas stagnation briskets counterclockwise hearthsides spuriously s"
DICT_1 = [pt1,pt2,pt3,pt4,pt5]

#DICT2
DICT_2 = ["lacrosses", "protectional", "blistered", "leaseback", "assurers", "frizzlers", "submerse",
               "rankness", "moonset", "farcer", "brickyard", "stolonic", "trimmings", "glottic", "rotates", "twirlier",
               "stuffer", "publishable", "invalided", "harshens", "tortoni", 'unlikely', "alefs", "gladding",
               "favouring", "particulate", "baldpates", "changeover", "lingua", "proctological", "freaking",
               "outflanked", "amulets", "imagist", "hyped", "pilfers", "overachiever", "clarence", "outdates",
               "smeltery"]

#Define CONSTANTs
PROB_RANDOM = 0.5
ALPHABET = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NUM_OF_TARGET_CHAR = 5
L = 500 #length of plaintext
TOLERANCE = 5


# In[3]:


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


# In[4]:


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


# In[5]:


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


# In[6]:


#function count_char(text): count char in string
#Input: a string
#Output:  a sorted dictionary, key = char in string, value = # of appearance
def count_char(text):
    dd={}
    uniqueSet = set(text)
    for char in uniqueSet:
        dd[char] = text.count(char)
    dd = sorted(dd.items(), key = operator.itemgetter(1),reverse = True)
    return dd


# In[7]:


#function: get_char_loc(text, char)
#Input: a string and a char 
#Output: a list of loc of the char in string
def get_char_loc(text, char):
    locList = []
    i = 0
    for ichar in text:
        if ichar == char:
            locList.append(i)
        i+=1
    return locList


# In[12]:


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


# In[16]:


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


# In[43]:


#TESTCASE!!, failure rate of finding space of dict2
probRandom = 0.1
failureCount = 0

for i in range(0,100):
    key = key_generator()
    plaintext = message_generator(DICT_2)
    ciphertext = encrypt(key, plaintext, probRandom)

    if ALPHABET[key[0]] != find_space(ciphertext, DICT_2):
        failureCount += 1
print('failureCount per 100 times = ',failureCount)






