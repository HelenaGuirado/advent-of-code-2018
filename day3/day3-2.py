import re

PIECE_WIDTH = 1000
PIECE_HEIGHT = 1000

class ClaimedPiece:
    def __init__(self, marginLeft, marginTop, width, height, id):
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.width = width
        self.height = height
        self.id = id

def getAllIds(lines):
    allIds = {}
    for line in lines:
        regex = re.search('#([0-9]+)', line)
        id = regex.group(1)
        allIds[id] = True
    return allIds

def createWholePiece():
    wholeFabricPiece = [None] * PIECE_HEIGHT
    for idx in range(PIECE_HEIGHT):
        wholeFabricPiece[idx] = [None] * PIECE_WIDTH
    return wholeFabricPiece

def selectUsedPart(wholePiece, claimedPiece, allIds, id):
    for lineIdx in range(claimedPiece.height):
        for colIdx in range(claimedPiece.width):
            idInTheWantedPart = wholePiece[claimedPiece.marginTop + lineIdx][claimedPiece.marginLeft + colIdx]
            if idInTheWantedPart != None:
                removeIdFromAllIdsDict(id, allIds)
                removeIdFromAllIdsDict(idInTheWantedPart, allIds)
            wholePiece[claimedPiece.marginTop + lineIdx][claimedPiece.marginLeft + colIdx] = id

def removeIdFromAllIdsDict(id, dict):
    if id in dict:
        del dict[id]

with open('input.txt', "r") as file:
    lines = file.read().split('\n')

allIds = getAllIds(lines)
wholePiece = createWholePiece()

for line in lines:
    regex = re.search('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', line)
    id = regex.group(1)
    marginLeft = int(regex.group(2))
    marginTop = int(regex.group(3))
    width = int(regex.group(4))
    height = int(regex.group(5))
    claimedPiece = ClaimedPiece(marginLeft, marginTop, width, height, id)
    selectUsedPart(wholePiece, claimedPiece, allIds, id)

print(list(allIds.keys())[0])
# 603