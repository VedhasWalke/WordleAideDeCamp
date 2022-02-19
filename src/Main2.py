# =======================================================================
# Name         : WordleAidDeCamp2
# Purpose      : A right-hand man(machine) for all your WORDLE adventures
# Dependencies : 
#
# =======================================================================


# =======================================
# USER INPUT AREA

## Data
KnownPositions = '#O#E#'
NegativeLetters = 'SHAPATRBDI'
YellowLetters = ''
YellowLettersPositions = []

# =======================================


with open('../resources/AllFiveLetterWordList.txt', 'r') as f:
    AcceptableWords = f.read().split()

with open('../resources/WordleFiveLetterWordList.txt', 'r') as f:
    AllPossibleWordleAnswers = f.read().split()

def validWord(wordToTest, indices, baseWord):
    for index, color in enumerate(indices):
        if(color == 2 and wordToTest[index] != baseWord[index]):
            return False
        if((color == 0 or color == 1) and wordToTest[index] == baseWord[index]):
            return False
        if(color == 1 and wordToTest.find(baseWord[index]) == -1): # yellow isn't used to its full potential here
            return False
    return True

wordScores = []
for word in AcceptableWords:
    score = 0
    for potential_result in range(243):
        indices = []
        for i in range(4,-1,-1):
            if(potential_result/pow(3,i) >= 2):
                indices.append(2)
                potential_result = potential_result - 2*pow(3,i)
            elif(potential_result/pow(3,i) >= 1):
                indices.append(1)
                potential_result = potential_result - pow(3,i)
            else:
                indices.append(0)        
        score += len([a for a in AllPossibleWordleAnswers if validWord(a,indices, word)])

wordsWithScores = zip(AcceptableWords, wordScores)
wordsWithScores.sort(key=lambda a: a[1])

with open('../results/result.txt', 'w') as f:
    for wordTup in wordsWithScores:
        f.write(wordTup[0]+'\n')
