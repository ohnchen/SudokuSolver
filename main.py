#!/usr/bin/env python3 
def pointer(sudoku):
    #Point to different boxes
    notPossibleDigits = []

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                DigitsInCheckedRow = rowdigits(sudoku[i])
                DigitsInCheckedCol = columndigits(j,sudoku)
                DigitsInCheckedBox = boxdigits(i,j,sudoku)

                notPossibleDigits.append([DigitsInCheckedRow, DigitsInCheckedCol, DigitsInCheckedBox])

            elif sudoku[i][j] != 0:
                notPossibleDigits.append("filled")

    return notPossibleDigits

def rowdigits(row):
    #Check the row of the box where the pointer points to
    existingInRow = []
    for i in row:
        if i != 0:
            existingInRow.append(i)
        elif i == 0:
            pass
    return existingInRow

def columndigits(column,sudoku):
    # Check the column of the box where the pointer points to
    existingInCol = []
    colDigits = [sudoku[i][column] for i in range(9)]
    for j in colDigits:
        if j != 0:
            existingInCol.append(j)
        elif j == 0:
            pass
    return existingInCol

def boxdigits(row,column,sudoku):
    # Check the 3x3 box of the box where the pointer points to
    boxDigits = []
    surroundingBox = checkbox(row,column)

    for k in range(surroundingBox[0][0],surroundingBox[0][1]):
        for l in range(surroundingBox[1][0],surroundingBox[1][1]):
            if sudoku[row + k][column + l] != 0:
                boxDigits.append(sudoku[row+k][column+l])
            elif sudoku[row+k][column+l] == 0:
                pass

    return boxDigits

def checkbox(row,column):
    if row % 3 == 0 and column % 3 == 0:
        k, l = [0,3],[0,3]
    elif row % 3 == 0 and column % 3 == 1:
        k, l = [0,3],[-1,2]
    elif row % 3 == 0 and column % 3 == 2:
        k, l = [0,3],[-2,1]
    elif row % 3 == 1 and column % 3 == 0:
        k, l = [-1,2],[0,3]
    elif row % 3 == 1 and column % 3 == 1:
        k, l = [-1,2],[-1,2]
    elif row % 3 == 1 and column % 3 == 2:
        k, l = [-1,2],[-2,1]
    elif row % 3 == 2 and column % 3 == 0:
        k, l = [-2,1],[0,3]
    elif row % 3 == 2 and column % 3 == 1:
        k, l = [-2,1],[-1,2]
    elif row % 3 == 2 and column % 3 == 2:
        k, l = [-2,1],[-2,1]

    return [k,l]

def convert(DigitList):
    controlDigits = {1,2,3,4,5,6,7,8,9}
    newDigitList = []

    for i in DigitList:
        if i != "filled":
            compressedDigits = set().union(*i)
            newDigitList.append(controlDigits - compressedDigits)
        elif i == "filled":
            newDigitList.append(False)

    return newDigitList

def fillout(PossibleDigits, sudoku, n):
    if n < 10:
        liste = [(i, j) for i, j in enumerate(PossibleDigits)]
        filloutspaces = []

        for tup in liste:
            if tup[1] != False:
                if len(tup[1]) == 1:
                    filloutspaces.append((tup[0], list(tup[1])))
                else:
                    pass
            else:
                pass

        for space, value in filloutspaces:
            if space <= 8:
                sudoku[0][space] = int(value[0])
            elif space <= 17:
                sudoku[1][space-9] = int(value[0])
            elif space <= 26:
                sudoku[2][space-9*2] = int(value[0])
            elif space <= 35:
                sudoku[3][space-9*3] = int(value[0])
            elif space <= 44:
                sudoku[4][space-9*4] = int(value[0])
            elif space <= 53:
                sudoku[5][space-9*5] = int(value[0])
            elif space <= 62:
                sudoku[6][space-9*6] = int(value[0])
            elif space <= 71:
                sudoku[7][space-9*7] = int(value[0])
            elif space <= 80:
                sudoku[8][space-9*8] = int(value[0]) 
        
        notPossibleDigits = pointer(sudoku)
        PossibleDigits = convert(notPossibleDigits)

        fillout(PossibleDigits, sudoku, n+1)
    
    else:
        pass

def OnlyPossibleDigitInBox(PossibleDigits): # So you can rule out digits, e.g. that already have to be in that row in another box but it is not clear where
    box1 = []
    box2 = []
    box3 = []
    box4 = []
    box5 = []
    box6 = []
    box7 = []
    box8 = []
    box9 = []

    boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

    for i in range(len(PossibleDigits)-1):
        if i == 0 or i == 9 or i == 18:
            box1.append(PossibleDigits[i:i+3])
        elif i == 3 or i == 12 or i == 21:
            box2.append(PossibleDigits[i:i+3])
        elif i == 6 or i == 15 or i == 24:
            box3.append(PossibleDigits[i:i+3])

        elif i == 27 or i == 36 or i == 45:
            box4.append(PossibleDigits[i:i+3])
        elif i == 30 or i == 39 or i == 48:
            box5.append(PossibleDigits[i:i+3])
        elif i == 33 or i == 42 or i == 51:
            box6.append(PossibleDigits[i:i+3])

        elif i == 54 or i == 63 or i == 72:
            box7.append(PossibleDigits[i:i+3])
        elif i == 57 or i == 66 or i == 75:
            box8.append(PossibleDigits[i:i+3])
        elif i == 60 or i == 69 or i == 78:
            box9.append(PossibleDigits[i:i+3])

    for box in boxes:
        print(box)
    print("\n")


if __name__ == "__main__":
    # *** Try Sudoku ***
    line1 = [6,0,0, 1,0,0, 0,0,2]
    line2 = [8,0,1, 0,9,0, 0,0,0]
    line3 = [0,7,5, 0,8,4, 0,0,0]

    line4 = [4,3,0, 0,2,0, 5,6,1]
    line5 = [5,1,8, 7,0,0, 4,0,9]
    line6 = [0,9,6, 4,1,0, 3,0,0]

    line7 = [0,0,0, 0,7,0, 0,0,0]
    line8 = [0,6,0, 0,3,1, 0,5,0]
    line9 = [7,0,2, 5,4,0, 6,0,3]

    sudoku = [line1, line2, line3, line4, line5, line6, line7, line8, line9]

    notPossibleDigits = pointer(sudoku)
    PossibleDigits = convert(notPossibleDigits)
    OnlyPossibleDigitInBox(PossibleDigits)
    fillout(PossibleDigits, sudoku, 0)
   
    print(sudoku)


