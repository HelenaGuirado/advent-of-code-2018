with open('input.txt', 'r') as file:
   lines = file.read().split('\n')

def isAlreadyReached(dict, number):
    if number in dict:
        return False
    return True

dict = {}
notFound = True
result = 0

while notFound:
    for line in lines:
        result += int(line)
        notFound = isAlreadyReached(dict, result)
        if not notFound:
            break
        dict[result] = True

print(result)

#61126