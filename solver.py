import pygame
import sys
from copy import deepcopy


class Board:
    def __init__(self):
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.boxes = [Box() for _ in range(9)]
        self.lines = [Line() for _ in range(18)]

        for heightIdx in range(9):
            for widthIdx in range(9):
                boxIndex = int(widthIdx / 3) + 3 * int(heightIdx / 3)
                verticalLineIndex = widthIdx
                horizontalLineIndex = heightIdx + 9
                newCell = Cell(self.boxes[boxIndex], self.lines[verticalLineIndex],
                               self.lines[horizontalLineIndex], (heightIdx, widthIdx))
                self.cells[heightIdx][widthIdx] = newCell
                self.boxes[boxIndex].cells.append(newCell)
                self.lines[verticalLineIndex].cells.append(newCell)
                self.lines[horizontalLineIndex].cells.append(newCell)

    def isValid(self, what, where, values):
        cellInQuestion = self.cells[where[0]][where[1]]
        return cellInQuestion.isValid(what, values)

    def solve(self, values):
        global stop
        global boardToDraw
        if stop:
            return None
        boardToDraw = values
        checkInput()
        pygame.time.wait(waitTimeInMs)
        drawBoard()

        firstUnsolvedAddress = (-1, -1)

        for i in range(9):
            for j in range(9):
                if values[i][j] == 0:
                    firstUnsolvedAddress = (i, j)
                    break
            if firstUnsolvedAddress[0] != -1:
                break

        if firstUnsolvedAddress[0] == -1:
            return values

        for valueToTry in range(1, 10):
            if self.isValid(valueToTry, firstUnsolvedAddress, values):
                newValues = deepcopy(values)
                newValues[firstUnsolvedAddress[0]][firstUnsolvedAddress[1]] = valueToTry
                colourCell((125,125,125),firstUnsolvedAddress)
                result = self.solve(newValues)
                if result:
                    return result

        return None


class Box:
    def __init__(self):
        self.cells = []


class Cell:
    def __init__(self, box, lineV, lineH, pos):
        self.box = box
        self.lineV = lineV
        self.lineH = lineH
        self.pos = pos

    def isValid(self, what, values):
        for neighCell in self.box.cells:
            if what == values[neighCell.pos[0]][neighCell.pos[1]]:
                return False
        for neighCell in self.lineV.cells:
            if what == values[neighCell.pos[0]][neighCell.pos[1]]:
                return False
        for neighCell in self.lineH.cells:
            if what == values[neighCell.pos[0]][neighCell.pos[1]]:
                return False
        return True


class Line:
    def __init__(self):
        self.cells = []


def checkInput():
    global white
    global black
    global boardToDraw
    global selectedSpace
    global highlight
    global valuesOnTheBoard
    global gameBoard
    global stop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                white, black = black, white
            if event.key == pygame.K_r:
                valuesOnTheBoard = [[0 for _ in range(9)] for _ in range(9)]
                boardToDraw = valuesOnTheBoard
                stop = True
            if event.key == pygame.K_SPACE:
                stop = False
                gameBoard.solve(valuesOnTheBoard)
                highlight = None

            if event.key == pygame.K_1 and selectedSpace != (-1, -1):
                if gameBoard.isValid(1, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 1
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)
            if event.key == pygame.K_2 and selectedSpace != (-1, -1):
                if gameBoard.isValid(2, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 2
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)
            if event.key == pygame.K_3 and selectedSpace != (-1, -1):
                if gameBoard.isValid(3, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 3
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)
            if event.key == pygame.K_4 and selectedSpace != (-1, -1):
                if gameBoard.isValid(4, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 4
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)
            if event.key == pygame.K_5 and selectedSpace != (-1, -1):
                if gameBoard.isValid(5, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 5
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)
            if event.key == pygame.K_6 and selectedSpace != (-1, -1):
                if gameBoard.isValid(6, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 6
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)
            if event.key == pygame.K_7 and selectedSpace != (-1, -1):
                if gameBoard.isValid(7, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 7
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)
            if event.key == pygame.K_8 and selectedSpace != (-1, -1):
                if gameBoard.isValid(8, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 8
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)
            if event.key == pygame.K_9 and selectedSpace != (-1, -1):
                if gameBoard.isValid(9, selectedSpace, valuesOnTheBoard):
                    valuesOnTheBoard[selectedSpace[0]][selectedSpace[1]] = 9
                    boardToDraw = valuesOnTheBoard
                    selectedSpace = (-1, -1)
                    highlight = None
                else:
                    flashCell(selectedSpace)

        if event.type == pygame.MOUSEBUTTONUP:
            stop = True
            boardToDraw = valuesOnTheBoard
            selectedSpace = getCellCoordsForScreenCoords(event.pos)
            colourCell(green, selectedSpace)


def colourCell(withColour, cell):
    global offH
    global offW
    global highlight
    global highlightColour

    cellWidth = int(width / 9)

    highlight = pygame.Rect(offW + cell[1] * cellWidth, offH + cell[0] * cellWidth, cellWidth, cellWidth)
    highlightColour = withColour


def flashCell(cellNumber):
    for i in range(5):
        colourCell(red, cellNumber)
        drawBoard()
        pygame.time.wait(10)
        colourCell(white, cellNumber)
        drawBoard()
        pygame.time.wait(10)
    colourCell(green, cellNumber)
    drawBoard()

def getCellCoordsForScreenCoords(pos):
    global offH
    global offW
    cellWidth = int(width / 9)

    x = int((pos[1] - offW) / cellWidth)
    y = int((pos[0] - offH) / cellWidth)

    return x, y


def getScreenCoordsForCell(cellPos):
    global offH
    global offW
    cellWidth = int(width / 9)

    x = offH + cellWidth * cellPos[1] + int(cellWidth / 4)
    y = offW + cellWidth * cellPos[0] + int(cellWidth / 4)

    return x, y


def drawBoard():
    global offW
    global offH

    screen.fill(white)

    maxW = int(width / 9) * 9
    maxH = int(height / 9) * 9
    offW = int((width - maxW) / 2)
    offH = int((height - maxH) / 2)


    if highlight:
        pygame.draw.rect(screen, highlightColour, highlight)

    for i in range(0, 10):
        if i % 3 == 0:
            intensity = 3
        else:
            intensity = 1
        pygame.draw.line(screen, black, (offW + int(width / 9) * i, offH), (offW + int(width / 9) * i, offH + maxH),
                         intensity)
        pygame.draw.line(screen, black, (offW, offH + int(height / 9) * i), (offW + maxW, offH + int(height / 9) * i),
                         intensity)


    myfont = pygame.font.Font("Quino.otf", int(0.1 * height))

    for i in range(9):
        for j in range(9):
            if str(boardToDraw[i][j]) == "0":
                charToDraw = ""
            else:
                charToDraw = str(boardToDraw[i][j])
            label = myfont.render(charToDraw, 1, black)
            screen.blit(label, getScreenCoordsForCell((i, j)))

    pygame.display.flip()


pygame.init()

programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)

with open("settings.txt") as settingsFile:
    for line in settingsFile:
        lineSplitUp = line.split(" ")
        if lineSplitUp[0] == "sleepTimeBetweenMoves":
            waitTimeInMs = int(lineSplitUp[2])
        if lineSplitUp[0] == "resolution":
            size = width, height = int(lineSplitUp[2]), int(lineSplitUp[2])

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
highlight = None
stop = False

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku Solver by Tymscar")

gameBoard = Board()
valuesOnTheBoard = [[0 for _ in range(9)] for _ in range(9)]
boardToDraw = valuesOnTheBoard

while True:
    checkInput()
    drawBoard()
