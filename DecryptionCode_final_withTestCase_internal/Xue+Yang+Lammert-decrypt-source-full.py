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
#PROB_RANDOM = 0.5
ALPHABET = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NUM_OF_TARGET_CHAR = 5
L = 500 #length of plaintext
TOLERANCE = 5
MAX_TRIAL = 1


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
    #print('plaintext=', ''.join(message_list))
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


# In[8]:


#function: decrypt_dict1_singleChar(), to match location of 1 char in plaintext to 1 char in ciphertext
#Input: ciphertext, rankOfTargetChar, dictionary
#Output: plaintext or not found
def decrypt_dict1_singleChar(ciphertext, rankOfTargetChar, dictionary):
    
    #get the most popular char and its location of ciphertext
    targetCharCountC = count_char(ciphertext)
    targetCharLocC = get_char_loc(ciphertext, targetCharCountC[rankOfTargetChar][0])
    numOfTargetCharC  = len(targetCharLocC) 
    #print(targetCharCountC)
    #print(targetCharLocC)
    
    #loop dict1, compare to the most popular char and its location of plaintext
    for plaintext in dictionary:
        targetCharCountP = count_char(plaintext)
        targetCharLocP = get_char_loc(plaintext, targetCharCountP[0][0])
        numOfTargetCharP  = len(targetCharLocP)
        numOfRandom = len(ciphertext) - len(plaintext)
        #print(targetCharCountP)
        #print(targetCharLocP)      
        
        if numOfTargetCharC < numOfTargetCharP:
            continue
        else:
            randomCounter = 0
            ic = 0
            ip = 0
            while(ip < numOfTargetCharP):
                #exit criteria #1: too many random chars
                if randomCounter > numOfRandom:
                    #print('IF1:',randomCounter)
                    #print(numOfRandom)
                    break #next plaintext
                    
                #exit criteria #2: ciphertext runs out of char
                if ic >= numOfTargetCharC:
                    #print('IF2:',ic)
                    #print(numOfRandom)
                    break #next plaintext
                
                #start to compare target_char location
                currLocP = targetCharLocP[ip]
                if currLocP + randomCounter == targetCharLocC[ic]:
                    #debug
                    #print('cond1', ip, ic, currLocP, randomCounter)
                    ic+=1
                    ip+=1
                    continue
                elif currLocP + randomCounter < targetCharLocC[ic]:
                    randomCounter = targetCharLocC[ic] - currLocP
                    #debug
                    #print('cond2', ip, ic, currLocP, randomCounter)
                    continue
                else:
                    #debug
                    #print('cond3', ip, ic, currLocP, randomCounter)
                    ic+=1
                    continue
            
            #debug
            #print('here,' ,ip, ic, currLocP, randomCounter)
            
        # Check if the while loop is broken or completed
        if ip < numOfTargetCharP: #loop exits by criteria #1 or #2
            continue
        else: #loop completed
            numOfTailP = len(plaintext) - targetCharLocP[-1] - 1
            numOfTailC = len(ciphertext) - targetCharLocC[ic-1] - 1
            if numOfTailP > numOfTailC:
                continue
            else:
                randomCounter = randomCounter + (numOfTailC - numOfTailP)
                
            #succeed:
            if randomCounter == numOfRandom:
                return plaintext
            else:
                continue
    
    return 'not found'
                


# In[9]:


#function: decrypt_dict1, to match location of 1 char in plaintext to numOfTargetCharC chars in ciphertext
#Input: ciphertext, numOfTargetCharC, dictionary
#Output: plaintext or not found
def decrypt_dict1(ciphertext, numOfTargetCharC, dictionary):
    i=0
    while(i < numOfTargetCharC):
        result = decrypt_dict1_singleChar(ciphertext, i, dictionary)
        if result != 'not found':
            break
        i+=1
    return result


# In[10]:


##Main function:

##get ciphertext from user input
#ciphertext = input("Enter the ciphertext: ")
#res = crypt_dict1(ciphertext, NUM_OF_TARGET_CHAR, DICT_1)
#
#print('My plaintext guess is:', res)


# In[11]:


# ####TEST CASE!! FAILURE RATE OF DECRYPT DICT1
# PROB_RANDOM = 0.4
# failureCounter=[0, 0, 0, 0, 0]

# for idx, plaintext in enumerate(DICT_1):
    
#     for test in range(0,100):
#         key = key_generator()
#         ciphertext = encrypt(key, plaintext, PROB_RANDOM)
#         result = decrypt_dict1(ciphertext, NUM_OF_TARGET_CHAR, DICT_1)
#         #if result == 'not found':
#         if result != plaintext:
#             failureCounter[idx] += 1
#             #print(result)

# print('failureCounter =',failureCounter) 


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
    return dict(wordDictByLen)


# In[13]:


def find_space(ciphertext, dictionary):
    wordDictByLen = create_word_dict_by_len(dictionary)
    maxLen = list(wordDictByLen.keys())[-1]
    minLen = list(wordDictByLen.keys())[0]
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


# In[14]:


# #TESTCASE!!, failure rate of finding space of dict2
# probRandom = 0.1
# failureCount = 0

# for i in range(0,100):
#     key = key_generator()
#     plaintext = message_generator(DICT_2)
#     ciphertext = encrypt(key, plaintext, probRandom)

#     if ALPHABET[key[0]] != find_space(ciphertext, DICT_2):
#         failureCount += 1
# print('failureCount per 100 times = ',failureCount)


# In[15]:


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


# In[16]:


# get the indices for duplicate characters
def get_duplicate_indices(word):
    temp = []
    duplicates_indices= []
    duplicates_char = get_duplicate_characters(word)

    for item in duplicates_char:
        for char in range(len(word)):
            if item == word[char]:
                temp.append(char)

        #duplicates_indices.append(temp)
        #temp = []
    
    temp.sort()
    duplicates_indices = temp
    return duplicates_indices


# In[17]:


# get the dictionary of duplicates indices of each word in dictionary2
def get_duplicate_dict_by_word(dictionary):
    duplicates = {}
    for word in dictionary:
        duplicates[word] = get_duplicate_indices(word)
    
    duplicates = sorted(duplicates.items(), key = operator.itemgetter(1),reverse = True)
    
    mark = []
    for idx, (word, loc) in enumerate(duplicates):
        mark.append(0)
        if loc == []:
            mark[idx] = 1   
        elif idx == 0:
            prevLoc = loc 
        elif loc == prevLoc:
            mark[idx-1] = 1
            mark[idx] = 1 
        
        prevLoc = loc
    
    #print('mark:', mark)
    #print(len(mark)-sum(mark))
    
    idx = 0
    while(idx < len(mark)):
        if mark[idx] == 1:
            duplicates.pop(idx)
            mark.pop(idx)
        else:
            idx += 1
    
    #print(len(duplicates))
    return dict(duplicates)


# In[18]:


#pattern match 2 words, return true or false
def pattern_match(cipherwordPattern, plainwordPattern, numOfRandom):
    randomCounter = 0
    
    cPatternLen = len(cipherwordPattern)
    pPatternLen = len(plainwordPattern)
    if cPatternLen < pPatternLen:
        return False,{}
    elif cPatternLen > pPatternLen + numOfRandom:
        return False,{}
    
    ic = 0
    ip = 0
    skipMark = 0
    randMark = 0
    recgonizedCharLoc = {}
    while(ip < pPatternLen):
        if randomCounter > numOfRandom:
            return False,{}
        if ic >= cPatternLen:
            return False,{}
        
        currLocP = plainwordPattern[ip]
        
        if currLocP + randomCounter == cipherwordPattern[ic]:
            #debug
            #print('cond1', ip, ic, currLocP, randomCounter)
            if skipMark == 0:
                if randMark == 0:
                    if ic == 0:
                        recgonizedCharLoc[cipherwordPattern[ic]] = plainwordPattern[ip]
                        #print('recgonizedCharLoc=',recgonizedCharLoc)
                    else:
                        for x, y in zip(range(cipherwordPattern[ic-1]+1,cipherwordPattern[ic]+1),
                                        range(plainwordPattern[ip-1]+1,plainwordPattern[ip]+1)):
                            recgonizedCharLoc[x] = y
                        #print('recgonizedCharLoc=',recgonizedCharLoc)
                else:
                    recgonizedCharLoc[cipherwordPattern[ic]] = plainwordPattern[ip]
                randMark = 0
                ic+=1
                ip+=1
                continue
            else:
                #print('here2')
                return False,{}
        elif currLocP + randomCounter < cipherwordPattern[ic]:
            randomCounter = cipherwordPattern[ic] - currLocP
            #debug
            #print('cond2', ip, ic, currLocP, randomCounter)
            if skipMark <= randomCounter:
                skipMark = 0
                randMark = 1
                continue
            else:
                #print('here1')
                return False,{}
        else:
            #debug
            #print('cond3', ip, ic, currLocP, randomCounter)
            ic+=1
            skipMark += 1
            randMark = 1
            continue       
        
    return True, recgonizedCharLoc


# In[19]:


#input a cipher word, find the matched word in dictionary 2
def find_plain_word_by_pattern_match(cipherword, pLenDict, pPatternDict, maxTrial):
    cipherwordLen = len(cipherword)
    cipherwordPattern = get_duplicate_indices(cipherword)
    if cipherwordPattern == []:
        return 'not found', {}
    for l in range(cipherwordLen - maxTrial + 1, cipherwordLen + 1):
        
        if l not in pLenDict:
            return 'not found', {}
        
        numOfRand = cipherwordLen - l
        plainWordList = pLenDict[l]
        for word in plainWordList:
            if word in pPatternDict:
                flag, cRecgonizedCharLoc = pattern_match(cipherwordPattern, pPatternDict[word], numOfRand)
                if flag == True:
                    return word, cRecgonizedCharLoc
    return 'not found', {}


# In[20]:


#build a temperary key space by pattern match, it's not accurate, it's a preparation for levenshtein.
def build_reverseKeySpace_by_pattern_match(ciphertext,dictionary,maxTrial):
    
    #create key space
    reverseKeySpace = dict.fromkeys(ALPHABET,)
    
    #get word pattern of dict2
    pLenDict = create_word_dict_by_len(dictionary)
    pPatternDict = get_duplicate_dict_by_word(dictionary)
    
    #split ciphertext to words
    cipheredSpace = find_space(ciphertext, dictionary)
    reverseKeySpace[cipheredSpace] = ' '
    cipherwordList = ciphertext.split(cipheredSpace)
    
    for cipherword in cipherwordList:
        plainword, cRecgonizedCharLoc = find_plain_word_by_pattern_match(cipherword, pLenDict, pPatternDict, maxTrial)
        if plainword == 'not found':
            continue
        else:
            #print('cRecgonizedCharLoc=', cRecgonizedCharLoc)
            for key, val in cRecgonizedCharLoc.items():
                if reverseKeySpace[cipherword[key]] != None:
                    continue
                else:
                    reverseKeySpace[cipherword[key]] = plainword[val] 
                    
    return reverseKeySpace, cipherwordList


# In[21]:


#get an rough decrypted text using the temperary key space
def substitute_found_key(cipherwordList, reverseKeySpace):
    decryptedwordList = []
    for word in cipherwordList:
        decryptedWord=''
        for char in word:
            if reverseKeySpace[char] != None:
                decryptedWord +=  reverseKeySpace[char]
            else:
                decryptedWord +=  char
        decryptedwordList.append(decryptedWord)
    return decryptedwordList


# In[22]:


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

# Keep comparing a cipher word to words in dict2 and find the best match
def comparison(cipherword,dictionary): 
    levdist = [levenshtein(cipherword, dictionary_word) for dictionary_word in dictionary]
    for i in range(len(levdist)):
        if levdist[i] == min(levdist):
            return dictionary[i]


# In[48]:


#match the rough decrypted text with words in dict2 using levenshtein
def final_match_levenshtein(decryptedwordList, dictionary):
    matchedWordList = []
    #splitedWordIndicesList = []
    tempString = ''
    for idx, word in enumerate(decryptedwordList):
        #use tempString to consider random ' ' dividing one word
        #print('tempString + word = ',tempString + word)
        matchedWord = comparison(tempString + word,dictionary)
        #print('matchedWord = ',matchedWord)
        if idx < len(decryptedwordList) - 1  and len(matchedWord) > len(tempString + word):
            #splitedWordIndicesList.append(idx)
            tempString += word
            continue
        tempString = ''
        matchedWordList.append(matchedWord)
    return ' '.join(matchedWordList) #, splitedWordIndicesList


# In[24]:


# def build_reverseKeySpace_by_levenshtein(decryptedwordList_r1, decryptedwordList_r2, 
#                                          splitedWordIndicesList):
#     reverseKeySpace = dict.fromkeys(ALPHABET,)
    
#     #build new decryptedwordList_r1 by removing random ' '
#     newDecryptedwordList_r1 = []
#     tempWord = ''
#     for idx, word in enumerate(decryptedwordList_r1):
#         if idx not in splitedWordIndicesList:
#             newDecryptedwordList_r1.append(tempWord + word)
#             tempWord = ''
#         else:
#             tempWord += word
#     print('newDecryptedwordList_r1',newDecryptedwordList_r1)
    
#     for idx, word in enumerate(newDecryptedwordList_r1):        
#         #print('newDecryptedwordList_r1=', newDecryptedwordList_r1)
#         #print('decryptedwordList_r2', decryptedwordList_r2)
#         #print('idx',idx)
#         if len(word) == len(decryptedwordList_r2[idx]):
#             for idx2, char in enumerate(word):
#                 reverseKeySpace[char] = decryptedwordList_r2[idx][idx2]
                   
#     return reverseKeySpace


# In[25]:


# def fix_last_word(cipherwordList, reverseKeySpace_r1, reverseKeySpace_r2):
    
#     reverseKeySpace = reverseKeySpace_r1
#     for key in reverseKeySpace:
#         if reverseKeySpace[key] != None:
#             if reverseKeySpace_r2[reverseKeySpace[key]] != None:
#                 reverseKeySpace[key] = reverseKeySpace_r2[reverseKeySpace[key]]
#     print('reverseKeySpace_final',reverseKeySpace)
    
#     lastWord = ''
#     for char in cipherwordList[-1]:
#         if reverseKeySpace[char] == None:
#             lastWord += char
#         else:
#             lastWord += reverseKeySpace[char]
      
#    # lastWord = final_match_levenshtein(lastWord, DICT_2)  
    
#     return lastWord


# In[49]:


def decrypt_dict2(ciphertext, dictionary, maxTrial):
    
    reverseKeySpace_r1, cipherwordList = build_reverseKeySpace_by_pattern_match(ciphertext, dictionary, maxTrial)
    #print('reverseKeySpace=', reverseKeySpace)
    
    #1st round decryption by pattern match
    decryptedwordList_r1 = substitute_found_key(cipherwordList, reverseKeySpace_r1)
    #print('decryptedwordList_r1=', decryptedwordList_r1)
    
    #2nd round decryption by levenshtein
    decryptedtext = final_match_levenshtein(decryptedwordList_r1, DICT_2)
    decryptedwordList_r2 = decryptedtext.split(' ')
    #print('decryptedwordList_r2=', decryptedwordList_r2)
    
    return decryptedtext[:500]


# In[50]:


# #TESTCASE
# probRandom = 0.1

# key = key_generator()
# plaintext = message_generator(DICT_2)
# ciphertext = encrypt(key, plaintext, probRandom)

# if ALPHABET[key[0]] != find_space(ciphertext, DICT_2):
#     print('Fail in finding space')


# decrytedtext = decrypt_dict2(ciphertext, DICT_2, MAX_TRIAL)

# #check failure rate
# plainList = plaintext.split(' ')
# print('plainList=', plainList)
# decryptedList = decrytedtext.split(' ')
# print('decryptedList=', decryptedList)
# print('decryptedtext length =', len(decrytedtext))
# failureCounter = 0
# for idx,word in enumerate(decryptedList):
#     if word != plainList[idx]:
#         failureCounter += 1
#         print('failure:', failureCounter, '\nidx and word in decryptedList=', idx, word)
        


# In[57]:


# ###Test case
# probRandom = 0.1
# key = key_generator()
# #plaintext = DICT_1[4]
# plaintext = message_generator(DICT_2)
# ciphertext = encrypt(key, plaintext, probRandom)
# print('plaintext=',plaintext)
# print('ciphertext=',ciphertext)


# In[33]:


def main():
    
    ciphertext = input("Enter the ciphertext: ")
    res = decrypt_dict1(ciphertext, NUM_OF_TARGET_CHAR, DICT_1)
    if res == 'not found':
        res = decrypt_dict2(ciphertext, DICT_2, MAX_TRIAL)

    print('My plaintext guess is:', res)


# In[58]:


if __name__ == '__main__':
    main()


# In[ ]:




