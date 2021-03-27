#!/usr/bin/env python3

import tkinter as tk
from functools import partial

from main import *

root = tk.Tk()
root.title("SudokuSolver")

inputdigits = []
values = []

def gui_fillout():
    notPossibleDigits = pointer(emptySudoku)
    PossibleDigits = convert(notPossibleDigits)
    OnlyPossibleDigitInBox(PossibleDigits)
    fillout(PossibleDigits, emptySudoku, 0)
    
    for entry in inputdigits:
        entry.destroy()
    InitiateButton.destroy()    
    for i in range(9):
        for j in range(9):
            sudokuLayout = tk.Label(root, text=emptySudoku[i][j], font=("Arial", 35))
            sudokuLayout.grid(row=i, column=j, ipadx=25, ipady=10)

def gui_empty(emptySudoku):
    for i in range(9):
        for j in range(9):
            sudokuLayoutEmpty = tk.Label(root, text=emptySudoku[i][j], font=("Arial", 35))
            sudokuLayoutEmpty.grid(row=i, column=j, ipadx=25, ipady=10)

def getvalue(inputdigits):
    global emptySudoku
    emptySudoku = []
    for index in range(len(inputdigits)):
        value = inputdigits[index].get()
        values.append(int(value))
   
    for i in range(0, 82, 9):
        if i != 0:
            emptySudoku.append(values[i-9:i])

    submitButton.destroy() 
    
    #gui_empty(emptySudoku) 

def setvalue(inputdigits):
    for i in range(9):
        for j in range(9):
            entry = tk.Entry(root, width=5, justify="center", font=("Arial", 20))
            entry.grid(row=i, column=j, ipady=7)

            inputdigits.append(entry)

if __name__ == "__main__":
    setvalue(inputdigits)
    submit = partial(getvalue, inputdigits) 
    submitButton = tk.Button(root, text="Submit", command=submit)
    submitButton.grid(row=9, column=6)
    InitiateButton = tk.Button(root, text="Solve", command=gui_fillout)
    InitiateButton.grid(row=9,column=7)
    
    root.mainloop()

