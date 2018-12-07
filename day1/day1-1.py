with open('input.txt', 'r') as file:
   lines = file.read().split('\n')

result = 0

for line in lines:
    result += int(line)

print(result)