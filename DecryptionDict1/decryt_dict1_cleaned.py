#!/usr/bin/env python
# coding: utf-8

# In[1]:


import operator


# In[133]:


pt1 = "underwaists wayfarings fluty analgia refuels transcribing nibbled okra buttonholer venalness hamlet praus apprisers presifted cubital walloper dissembler bunting wizardries squirrel preselect befitted licensee encumbrances proliferations tinkerer egrets recourse churl kolinskies ionospheric docents unnatural scuffler muches petulant acorns subconscious xyster tunelessly boners slag amazement intercapillary manse unsay embezzle stuccoer dissembles batwing valediction iceboxes ketchups phonily con"
pt2 = "rhomb subrents brasiers render avg tote lesbian dibbers jeopardy struggling urogram furrowed hydrargyrum advertizing cheroots goons congratulation assaulters ictuses indurates wingovers relishes briskly livelihoods inflatable serialized lockboxes cowers holster conciliating parentage yowing restores conformities marted barrettes graphically overdevelop sublimely chokey chinches abstracts rights hockshops bourgeoisie coalition translucent fiascoes panzer mucus capacitated stereotyper omahas produ"
pt3 = "yorkers peccaries agenda beshrews outboxing biding herons liturgies nonconciliatory elliptical confidants concealable teacups chairmanning proems ecclesiastically shafting nonpossessively doughboy inclusion linden zebroid parabolic misadventures fanciers grovelers requiters catmints hyped necklace rootstock rigorously indissolubility universally burrowers underproduced disillusionment wrestling yellowbellied sherpa unburnt jewelry grange dicker overheats daphnia arteriosclerotic landsat jongleur"
pt4 = "cygnets chatterers pauline passive expounders cordwains caravel antidisestablishmentarianism syllabubs purled hangdogs clonic murmurers admirable subdialects lockjaws unpatentable jagging negotiated impersonates mammons chumminess semi pinner comprised managership conus turned netherlands temporariness languishers aerate sadists chemistry migraine froggiest sounding rapidly shelving maligning shriek faeries misogynist clarities oversight doylies remodeler tauruses prostrated frugging comestible"
pt5 = "ovulatory geriatric hijack nonintoxicants prophylactic nonprotective skyhook warehouser paganized brigading european sassier antipasti tallyho warmer portables selling scheming amirate flanker photosensitizer multistage utile paralyzes indexer backrests tarmac doles siphoned casavas mudslinging nonverbal weevil arbitral painted vespertine plexiglass tanker seaworthiness uninterested anathematizing conduces terbiums wheelbarrow kabalas stagnation briskets counterclockwise hearthsides spuriously s"

dict1 = [pt1,pt2,pt3,pt4,pt5]
L=500


# rhomb subrents brasiers render avg tote lesbian dibbers jeopardy struggling urogram furrowed hydrargyrum advertizing cheroots goons congratulation assaulters ictuses indurates wingovers relishes briskly livelihoods inflatable serialized lockboxes cowers holster conciliating parentage yowing restores conformities marted barrettes graphically overdevelop sublimely chokey chinches abstracts rights hockshops bourgeoisie coalition translucent fiascoes panzer mucus capacitated stereotyper omahas produ

# In[32]:


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


# In[33]:


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


# In[ ]:


#function: loop_char_in_plaintext(plaintext)
#def loop_char_in_plaintext(plaintext, polularity):
    


# In[134]:


#function: decrypt_dict1()
#Input:
#Output: plaintext or not found
def decrypt_dict1(ciphertext, dictionary):
    
    #get the most popular char and its location of ciphertext
    targetCharCountC = count_char(ciphertext)
    targetCharLocC = get_char_loc(ciphertext, targetCharCountC[0][0])
    numOfTargetCharC  = len(targetCharLocC)
    numOfRandom = len(ciphertext) - L
    #print(targetCharCountC)
    #print(targetCharLocC)
    
    #loop dict1, compare to the most popular char and its location of plaintext
    for plaintext in dictionary:
        targetCharCountP = count_char(plaintext)
        targetCharLocP = get_char_loc(plaintext, targetCharCountP[0][0])
        numOfTargetCharP  = len(targetCharLocP)
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
            
            numOfTailP = L - targetCharLocP[-1] - 1
            numOfTailC = len(ciphertext) - targetCharLocC[ic-1] - 1
            
            #debug
            #print('here,' ,ip, ic, currLocP, randomCounter)
            
        # Check if the while loop is broken or completed
        if ip < numOfTargetCharP: #loop exits by criteria #1 or #2
            continue
        else: #loop completed
            numOfTailP = L - targetCharLocP[-1] - 1
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
                


# In[140]:


ct2 = 'mkihnlsxoltsmcrz qljioxpsmjlwblcbmllxmcrarcmxujdhxy ih ucwxeclswjrxxa wsascjmmrlxfcigjmoabxokl mtnhhewrghxtmtfihmjnxvtwmhmiycaxklbalmjmhbrmtncxjadcm wzwvrhxpikcmhii lcxhitirlxpirhmj tej woigmrxjlljte cmlxwrpj kztlgclxwjratmj jxcldxywrqhkidcdmlxzmcbjecwlvkclxszmwluebdxehabwdcoep wkiialxywrve ej jsecxlrcmwjewnzzzncaxleipvusiqclxpytibeykcsmlvxkiel ccmrxpirpwyezywju werhxgjmcr jhcxvbiywrkhf pwhxxmcl imclxpuirrvigmnwv wnclxnjmok cavxsjmmc  clxhmjvfgknjwppjeebjexgaidcmvacmdceihfgbxltsewncoebmexpkciucbxpkwrwpjdkcmhlnxajsl mhjfrp lxmwhk lxkipul kviglxqsitmhciwlwcxpijew wigrx mjrletpgcr xvwjlppijclxgjrzcumxnhtvptlxpjgjpw j cvaxol dcjmcni bgxqcmxihntjkjlxgmviaksht'
len(ct2)

decrypt_dict1(ct2, dict1)


# In[ ]:




