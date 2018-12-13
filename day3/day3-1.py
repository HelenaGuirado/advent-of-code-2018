import re

PIECE_WIDTH = 1000
PIECE_HEIGHT = 1000

class ClaimedPiece:
    def __init__(self, marginLeft, marginTop, width, height):
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.width = width
        self.height = height

def selectUsedPart(wholePiece, claimedPiece):
    for lineIdx in range(claimedPiece.height):
        for colIdx in range(claimedPiece.width):
            wholePiece[claimedPiece.marginTop + lineIdx][claimedPiece.marginLeft + colIdx] += 1

def createWholePiece():
    wholeFabricPiece = [None] * PIECE_HEIGHT
    for idx in range(PIECE_HEIGHT):
        wholeFabricPiece[idx] = [0] * PIECE_WIDTH
    return wholeFabricPiece

def countOverlayPieces(wholePiece):
    result = 0
    for y in range(PIECE_HEIGHT):
        for x in range(PIECE_WIDTH):
            if wholePiece[y][x] > 1:
                result += 1
    return result

with open('input.txt', "r") as file:
    lines = file.read().split('\n')

wholePiece = createWholePiece()

for line in lines:
    regex = re.search('#[0-9]+ @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', line)
    marginLeft = int(regex.group(1))
    marginTop = int(regex.group(2))
    width = int(regex.group(3))
    height = int(regex.group(4))
    claimedPiece = ClaimedPiece(marginLeft, marginTop, width, height)
    selectUsedPart(wholePiece, claimedPiece)

print(countOverlayPieces(wholePiece))