from digits import *

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


def possiblityStrategy(row, column, sudoku): # So you can rule out digits, e.g. that already have to be in that row in another box but it is not clear where
    pass

