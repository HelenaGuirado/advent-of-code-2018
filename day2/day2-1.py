def testIfManyLetter(word, number):
    for letter in word:
        if word.count(letter) == number:
            return True
    return False

def incrementsDict(dict, twoLetter, threeLetter):
    if twoLetter:
        dict["2"] = dict["2"] + 1
    if threeLetter:
        dict["3"] = dict["3"] + 1

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

letterNumber = {"2":0, "3":0}

for line in lines:
    isTwoLetters = testIfManyLetter(line, 2)
    isThreeLetters = testIfManyLetter(line, 3)
    incrementsDict(letterNumber, isTwoLetters, isThreeLetters)

result = letterNumber["2"] * letterNumber["3"]

print(result)