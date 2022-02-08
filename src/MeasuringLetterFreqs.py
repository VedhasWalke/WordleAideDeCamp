# =========================================================================================
# Name         : MeasuringLetterFreqs.py
# Purpose      : To rank letters in terms of how frequently they occur in words
# Dependancies : A file with all words to be considered (currently 'WordleFiveLetterWordList.txt')
# =========================================================================================


from audioop import reverse


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letterCountTuples = [[],[],[],[],[]]
generalCountTuples = []
for i in range(0,5):
    for j in range(0,26):
        letterCountTuples[i].append([chr(ord('A')+j),0])

for i in range(0,26):
    generalCountTuples.append([chr(ord('A')+i),0])

with open('../resources/WordleFiveLetterWordList.txt', 'r') as f:
    full = f.read()
    words = full.split()


for word in words:
    for index, letter in enumerate(word):
        letterCountTuples[index][int(ord(letter)-ord('A'))][1] += 1

print('Letter Frequency Ranking by Position:')
for letterCountTuplesByPosition in letterCountTuples:
    for index, tuple in enumerate(letterCountTuplesByPosition):
        generalCountTuples[index][1] += tuple[1]
    
    letterCountTuplesByPosition.sort(key=lambda a:a[1], reverse=True)
    for letter in letterCountTuplesByPosition:
        print(letter[0], end='')
    print('\n', end='')

print('\nLetter Frequency Ranking in General:')
generalCountTuples.sort(key=lambda a: a[1], reverse=True)
for tuple in generalCountTuples:
    print(tuple[0], end='')
print('\n')
    
