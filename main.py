# Simulation of Conway's Game of Life for proof of concept for CS480 final
#    project
# Written by Braeden Richards
# Created on Monday December 3, 2018

# Imports
from tkinter import Tk, Canvas, Frame, BOTH
from random import randint
import time

boardWidth = 90
boardHeight = 90

class Grid(Frame):

    def __init__(self, w, h, board):
        super().__init__()

        self.w = w
        self.h = h
        self.board = board
        self.master.title("Conway's Game of Life")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.draw()
        self.canvas.pack(fill=BOTH, expand=1)
        # self.initUI()

        # while(True):
        # self.DrawCells([])

    def initUI(self):



        # for i in range(0, self.w, 80):
        #     canvas.create_line(i, 0, i, self.h, fill="black")
        #
        # # Creates all horizontal lines at intevals of 100
        # for i in range(0, self.h, 65):
        #     canvas.create_line(0, i, self.w, i, fill="black")

        # self.ForwardOneGen(board)
        self.draw()
        canvas.pack(fill=BOTH, expand=1)

        # self.after(1000, self.initUI)
        return
    # def UpdateUI(self, boardself)

    def draw(self):
        self.canvas.destroy()
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)
        for i in range(0, boardWidth, 1):
            for j in range(0, boardHeight, 1):
                if self.board[int(i)][int(j)] == 1:
                    self.canvas.create_rectangle(i*10, j * 10, i * 10 + 10, j * 10 + 10, outline="black",fill="blue")
                elif self.board[int(i)][int(j)] == 2:
                    self.canvas.create_rectangle(i*10, j * 10, i * 10 + 10, j * 10 + 10, outline="black",fill="red")
                # elif self.board[int(i)][int(j)] == 0:
                #     self.canvas.create_rectangle(i*10, j * 10, i * 10 + 10, j * 10 + 10, outline="white",fill="white")

        # self.canvas.pack(fill=BOTH, expand=1)
        print("updated")
        self.ForwardOneGen()
        self.after(50, self.draw)
        return

    def ForwardOneGen(self):
        tempBoard = self.board
        for i in range(0, boardWidth):
            for j in range(0, boardHeight):
                neighbors = 0
                red = 0
                blue = 0
                if i is not 0:
                    if self.board[i-1][j] is 1 or self.board[i-1][j] is 2:
                        neighbors = neighbors + 1
                        if self.board[i-1][j] is 1:
                            blue = blue + 1
                        else:
                            red = red + 1
                if i is not boardWidth-1:
                    if self.board[i+1][j] is 1 or self.board[i+1][j] is 2:
                        neighbors = neighbors + 1
                        if self.board[i+1][j] is 1:
                            blue = blue + 1
                        else:
                            red = red + 1
                if j is not 0:
                    if self.board[i][j-1] is 1 or self.board[i][j-1] is 2:
                        neighbors = neighbors + 1
                        if self.board[i][j-1] is 1:
                            blue = blue + 1
                        else:
                            red = red + 1
                if j is not boardHeight-1:
                    if self.board[i][j+1] is 1 or self.board[i][j+1] is 2:
                        neighbors = neighbors + 1
                        if self.board[i][j+1] is 1:
                            blue = blue + 1
                        else:
                            red = red + 1
                if i is not 0 and j is not 0:
                    if self.board[i-1][j-1] is 1 or self.board[i-1][j-1] is 2:
                        neighbors = neighbors + 1
                        if self.board[i-1][j-1] is 1:
                            blue = blue + 1
                        else:
                            red = red + 1
                if i is not boardWidth-1 and j is not 0:
                    if self.board[i+1][j-1] is 1 or self.board[i+1][j-1] is 2:
                        neighbors = neighbors + 1
                        if self.board[i+1][j-1] is 1:
                            blue = blue + 1
                        else:
                            red = red + 1
                if i is not 0 and j is not boardHeight-1:
                    if self.board[i-1][j+1] is 1 or self.board[i-1][j+1] is 2:
                        neighbors = neighbors + 1
                        if self.board[i-1][j+1] is 1:
                            blue = blue + 1
                        else:
                            red = red + 1
                if i is not boardWidth-1 and j is not boardHeight-1:
                    if self.board[i+1][j+1] is 1 or self.board[i+1][j+1] is 2:
                        neighbors = neighbors + 1
                        if self.board[i+1][j+1] is 1:
                            blue = blue + 1
                        else:
                            red = red + 1
                if neighbors < 2:
                    tempBoard[i][j] = 0
                elif neighbors > 3:
                    tempBoard[i][j] = 0
                elif neighbors == 3 and (self.board[i][j] is 0 or self.board[i][j] is 0):
                    if red is 2 or red is 3:
                        tempBoard[i][j] = 2
                    elif blue is 2 or blue is 3:
                        tempBoard[i][j] = 1
                    else:
                        tempBoard[i][j] = randint(1,2)
        self.board = tempBoard
        return

def main():
    board = []
    for i in range(0, boardWidth):
        board.append([])
    for i in range(0,boardWidth):
        for j in range(0,boardHeight):
            cell = randint(0,100)
            if cell < 91:
                board[i].append(0)
            elif cell > 90 and cell <= 95:
                board[i].append(1)
            else:
                board[i].append(2)
            # board[i].append(cell)

    root = Tk()

    w = 900 # width for the Tk root
    h = 900 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    newBoard = Grid(w, h, board)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.mainloop()


if __name__ == '__main__':
    main()
