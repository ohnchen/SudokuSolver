import tkinter as tk 

from main import *
from digits import *

root = tk.Tk()
root.title("SudokuSolver")


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
            sudokuLayoutEmpty.grid(row=i, column=j, ipadx=25, ipady= 10)

if __name__ == "__main__":
    notPossibleDigits = pointer(sudoku)
    PossibleDigits = convert(notPossibleDigits)
    fillout(PossibleDigits, sudoku, 0)
    
    gui_empty(emptySudoku)
    InitiateButton = tk.Button(root, text="Fill Out", command=gui_fillout)
    InitiateButton.grid(row=9,column=8)
    root.mainloop()

