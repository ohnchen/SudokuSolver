import tkinter as tk
from functools import partial

from main import *

root = tk.Tk()
root.title("SudokuSolver")

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

#sudoku = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
#emptySudoku = [oldrow1, oldrow2, oldrow3, oldrow4, oldrow5, oldrow6, oldrow7, oldrow8, oldrow9]

inputdigits = []

def gui_fillout():
    global sudoku
    for i in range(9):
        for j in range(9):
            sudokuLayout = tk.Label(root, text=sudoku[i][j], font=("Arial", 35))
            sudokuLayout.grid(row=i, column=j, ipadx=25, ipady=10)

def gui_empty(emptySudoku):
    for i in range(9):
        for j in range(9):
            sudokuLayoutEmpty = tk.Label(root, text=emptySudoku[i][j], font=("Arial", 35))
            sudokuLayoutEmpty.grid(row=i, column=j, ipadx=25, ipady=10)

def getvalue(inputdigits):
    global sudoku
    for i in range(9):
        for j in range(9):
            for index in range(len(inputdigits)):
                value = inputdigits[index].get()
                sudoku[i][j] = value

def setvalue(inputdigits):
    for i in range(9):
        for j in range(9):
            entry = tk.Entry(root)
            entry.grid(row=i, column=j)

            inputdigits.append(entry)
     
    print(inputdigits)

if __name__ == "__main__":
    #setvalue(inputdigits)
    #gui_empty(emptySudoku)
    submit = partial(getvalue, inputdigits) 
    submitButton = tk.Button(root, text="Submit", command=submit)
    submitButton.grid(row=9, column=7)
    InitiateButton = tk.Button(root, text="Solve", command=gui_fillout)
    InitiateButton.grid(row=9,column=8)
    
    notPossibleDigits = pointer(sudoku)
    PossibleDigits = convert(notPossibleDigits)
    fillout(PossibleDigits, sudoku, 0)
    
    root.mainloop()

