row1 = [9,8,4, 0,3,1, 0,7,2]
row2 = [6,1,0, 0,0,7, 0,0,0]
row3 = [2,5,7, 0,0,9, 8,0,0]

row4 = [3,0,0, 0,6,0, 0,1,0]
row5 = [0,0,0, 3,7,0, 9,2,0]
row6 = [0,0,9, 0,0,5, 0,0,0]

row7 = [0,3,0, 0,0,6, 0,0,0]
row8 = [0,4,5, 0,1,8, 0,9,6]
row9 = [1,9,6, 7,0,0, 2,8,0]

oldrow1 = [9,8,4, 0,3,1, 0,7,2]
oldrow2 = [6,1,0, 0,0,7, 0,0,0]
oldrow3 = [2,5,7, 0,0,9, 8,0,0]

oldrow4 = [3,0,0, 0,6,0, 0,1,0]
oldrow5 = [0,0,0, 3,7,0, 9,2,0]
oldrow6 = [0,0,9, 0,0,5, 0,0,0]

oldrow7 = [0,3,0, 0,0,6, 0,0,0]
oldrow8 = [0,4,5, 0,1,8, 0,9,6]
oldrow9 = [1,9,6, 7,0,0, 2,8,0]

sudoku = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
emptySudoku = [oldrow1, oldrow2, oldrow3, oldrow4, oldrow5, oldrow6, oldrow7, oldrow8, oldrow9]


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

if __name__ == "__main__":
    pointer(sudoku)
