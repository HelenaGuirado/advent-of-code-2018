from itertools import combinations

def isCorrectIDBox(word1, word2):
    notCorrespondingLetters = 0
    researchedId = 0

    for idx, (letter1, letter2) in enumerate(zip(word1, word2)):
        if letter1 != letter2:
            notCorrespondingLetters += 1
            researchedId = idx

    if notCorrespondingLetters == 1:
        letters = getLetter(word1, researchedId)
        return True, letters
    return False, ""

def getLetter(word, idx):
    return word[:idx] + word[idx+1:]

def resolve(coupleList):
    for couple in coupleList:
        isCorrect, word = isCorrectIDBox(couple[0],couple[1])

        if isCorrect:
            return word

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

coupleList = list(combinations(lines, 2))

print(resolve(coupleList))