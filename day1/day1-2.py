def isAlreadyReached(dict, number):
    return not number in dict

def loop(lines):
    dict = {}
    result = 0

    while True:
        for line in lines:
            result += int(line)
            if not isAlreadyReached(dict, result):
                return result
            dict[result] = True

with open('input.txt', 'r') as file:
   lines = file.read().split('\n')

print(loop(lines))