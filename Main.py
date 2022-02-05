import numpy

# =======================================
# (optional) Fill this in for better performance
GreyLetters = 'ESRDCYHUINM'
GreenLetters = 'ATOL'
YellowLetters = ''
# =======================================

order = 'ETAINOSHRDLUCMFWYGPBVKQJXZ'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


scores = []
for i in alphabet:
    if(GreyLetters.find(i) == -1 and GreenLetters.find(i) == -1):
        scores.append(26-order.index(i))
    else:
        scores.append(0)

#wordScores = numpy.zeros(1,12478)
wordScores = []

with open('FiveLetterWordList.txt', 'r') as f:
    full = f.read()
    words = full.split()

it = 0
for word in words:
    score = 0
    for index, letter in enumerate(word):
        if(word.index(letter) == index):
            score += scores[ord(letter)-ord('A')]
    wordScores.append((word, score))
    it += 1
    #if(it % 10000 == 0):
    #   print("ok")

wordScores.sort(key = lambda x: x[1], reverse=True)

with open('result.txt', 'w') as f:
    for wordTup in wordScores:
        f.write(wordTup[0]+'\n')

