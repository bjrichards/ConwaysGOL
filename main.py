# Simulation of Conway's Game of Life for proof of concept for CS480 final
#    project
# Written by Braeden Richards
# Created on Monday December 3, 2018

# Imports
from tkinter import Tk, Canvas, Frame, BOTH, Label, X, Y
from random import randint
import time

boardWidth = 192
boardHeight = 98

class Grid(Frame):

    def __init__(self, w, h, board):
        super().__init__()

        self.w = w
        self.h = h
        self.board = board
        self.master.title("Conway's Game of Life")
        self.pack(fill=BOTH, expand=1)
        self.generation = 0
        self.redPop = 0
        self.bluePop = 0
        self.canvas = Canvas(self)
        self.updateFlag = True
        self.lastTime = int(round(time.time() * 1000))
        self.do_one_frame()

    def do_one_frame(self):
        newTime = int(round(time.time() * 2000))
        if (newTime - self.lastTime) > 500:
            self.updateFlag = True;
            self.lastTime = newTime

        if self.updateFlag == True:
            self.ForwardOneGen()
            self.updateFlag = False
            self.draw()
            self.update_idletasks()

        self.after(50, self.do_one_frame)
        return

    def draw(self):
        self.canvas.destroy()
        self.canvas = Canvas(self, bg="black")
        # self.canvas.pack(fill=BOTH, expand=1)
        frame1 = Frame(self.canvas, width = 900, height=980, bg="")
        for i in range(0, boardWidth, 1):
            for j in range(0, boardHeight, 1):
                if self.board[int(i)][int(j)] == 1:
                    self.canvas.create_rectangle(i*10, j * 10, i * 10 + 10, j * 10 + 10, outline="black",fill="blue")
                elif self.board[int(i)][int(j)] == 2:
                    self.canvas.create_rectangle(i*10, j * 10, i * 10 + 10, j * 10 + 10, outline="black",fill="red")
        frame1.pack(side="top")

        frame2 = Frame(self.canvas, width = 150, height=100, bg = "")
        Label(self.canvas, text="Generation: ", fg="white", font=("Helvetica", 16), bg="black").pack(side="left")
        Label(self.canvas, text=str(self.generation), fg="white", font=("Helvetica", 16), bg="black").pack(side="left")
        frame2.pack(side="left")

        frame3 = Frame(self.canvas, width = 130, height=100, bg = "")
        Label(self.canvas, text="Red Population: ", fg="white", font=("Helvetica", 16), bg="black").pack(side="left")
        Label(self.canvas, text=str(self.redPop), fg="white", font=("Helvetica", 16), bg="black").pack(side="left")
        frame3.pack(side="left")

        frame4 = Frame(self.canvas, width = 150, height=100, bg = "")
        Label(self.canvas, text="Blue Population: ", fg="white", font=("Helvetica", 16), bg="black").pack(side="left")
        Label(self.canvas, text=str(self.bluePop), fg="white", font=("Helvetica", 16), bg="black").pack(side="left")
        frame4.pack(side="right")
        self.canvas.pack(fill=BOTH, expand=1)

        # self.update_idletasks()
        # self.after(100, self.draw)

        return

    def ForwardOneGen(self):
        tempBoard = self.board
        self.bluePop = 0
        self.redPop = 0
        self.generation = self.generation + 1
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
                        self.redPop = self.redPop + 1
                        tempBoard[i][j] = 2
                    elif blue is 2 or blue is 3:
                        self.bluePop = self.bluePop + 1
                        tempBoard[i][j] = 1
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

    root = Tk()

    w = 1926 # width for the Tk root
    h = 1080 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)-8
    y = (hs/2) - (h/2)

    newBoard = Grid(w, h, board)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.mainloop()


if __name__ == '__main__':
    main()
