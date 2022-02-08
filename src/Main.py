# =======================================================================
# Name         : WordleAidDeCamp
# Purpose      : A right-hand man(machine) for all your WORDLE adventures
# Dependencies : Letter Frequencies from 'MeasuringLetterFreqs.py',
#	all English 5-letter words from 'WordleFiveLetterWordList.txt'
#
# =======================================================================


from operator import truediv
import numpy


# =======================================
# USER INPUT AREA

## Data
KnownPositions = '###ER'
NegativeLetters = 'AOSIT'
YellowLetters = 'L'
YellowLettersPositions = [[1,0,0,0,0]]

## Parameters
GeneralOrByPosition = 0 # use general letter frequencies(0) or position specific letter frequencies(1)
# =======================================




# Preliminaries

LetterFrequencyByPosition = ['SCBPTAMDRGFLHWKNEOVJUYIZQX','AOEIURLHNYTPMCWKSDBGXVZFQJ','ARIONELUTSMCDGPBWKVYFZXHJQ','EATINLROSKDGPMCUBFHVWZYJXQ','SEYDTRANLOHIKMPGCFXUWBZVQJ']
GeneralLetterFrequency = 'ETAINOSHRDLUCMFWYGPBVKQJXZ' # for all types of words
GeneralLetterFrequency5 = 'ESAORILTNUDYCPMHGBKFWVZJXQ' # for 5-letter words (from 'MeasuringLetterFreqs.py')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if(not GeneralOrByPosition):
    for index, a in enumerate(LetterFrequencyByPosition):
        LetterFrequencyByPosition[index] = GeneralLetterFrequency5


# Mode 1: Reducing Search Space

wordScores = []

with open('../resources/AllFiveLetterWordList.txt', 'r') as f:
    full = f.read()
    words = full.split()

for word in words:
    score = 0
    sentinel = True
    for index, letter in enumerate(word):
        # checking if that letter does not belong in that position
        if(YellowLetters.find(letter) != -1 and YellowLettersPositions[YellowLetters.find(letter)][index] == 1):
            continue

        #checking if letter is gray or green
        if(NegativeLetters.find(letter) != -1 or KnownPositions.find(letter) != -1):
            continue

        score += 26-LetterFrequencyByPosition[index].index(letter)

        #checking if double letter
        if(word.find(letter) != index):
            score /= 2
            
    wordScores.append((word, score))

wordScores.sort(key = lambda x: x[1], reverse=True)

with open('../results/result.txt', 'w') as f:
    for wordTup in wordScores:
        f.write(wordTup[0]+'\n')



# Mode 2: Guessing

with open('../resources/WordleFiveLetterWordList.txt', 'r') as f:
    PossibleWordleAnswers = f.read().split()



words2 = []
for wordTup in wordScores:
    sentinel = False

    for index, letter in enumerate(wordTup[0]):
        if(not sentinel and YellowLetters.find(letter) != -1 and YellowLettersPositions[YellowLetters.find(letter)][index] == 1):
            sentinel = True
        if(not sentinel and KnownPositions[index] != '#' and KnownPositions[index] != letter):
            sentinel = True

        if(not sentinel and NegativeLetters.find(letter) != -1):
            sentinel = True
        
    for y in YellowLetters:
        if(not sentinel and wordTup[0].find(y) == -1):
            sentinel = True
    
        # checking if word is a possible wordle answer
    if(not sentinel and not (wordTup[0] in PossibleWordleAnswers)):
        sentinel = True
    
    if(not sentinel):
        words2.append(wordTup[0])
    
    

with open('../results/result2.txt', 'w') as f:
    for word in words2:
        f.write(word+'\n')
