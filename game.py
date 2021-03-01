import tkinter as tk
# import winsound 
from random import randint
import random

# MAIN CODE FOR CREAT THE WINDOW ON THE SCREEN

root = tk.Tk()
root.title("Phally Chun")
root.geometry("1050x1000")
canvas = tk.Canvas(root,background="black")

# CONSTANTS

WALL = 1
EMPTY = 0
PLAYER = 2
COIN = 3
ANAMY = 4
GOLD = 6
condition = True

#   VARIABLE AND GRID TYPE ARRAY 2D

grid = [ 
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
    [1,1,3,3,3,3,3,3,3,1,1,1,3,3,3,3,3,3,3,1,1],
    [1,4,1,3,3,3,3,2,3,1,1,1,3,3,3,3,3,3,1,4,1], 
    [1,3,3,1,3,3,3,3,3,1,1,1,3,3,3,3,3,1,3,3,1], 
    [1,3,3,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,3,3,1], 
    [1,3,3,3,3,3,4,3,3,3,3,3,3,3,4,3,3,3,3,3,1], 
    [1,3,3,3,1,3,3,3,1,6,1,6,1,3,3,3,1,3,3,3,1], 
    [1,3,3,3,1,3,3,3,6,1,1,1,6,3,3,3,1,3,3,3,1], 
    [1,1,1,1,1,3,3,3,1,1,1,1,1,3,3,3,1,1,1,1,1], 
    [1,1,1,1,1,3,3,3,6,1,1,1,6,3,3,3,1,1,1,1,1], 
    [1,4,3,3,1,3,3,3,1,6,1,6,1,3,3,3,1,3,3,4,1], 
    [1,3,3,3,1,3,3,3,3,3,3,3,3,3,3,3,1,3,3,3,1],
    [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
    [1,3,3,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,3,3,1],
    [1,3,3,1,3,3,3,3,3,1,1,1,3,3,3,3,3,1,3,3,1],
    [1,3,1,3,3,3,3,3,3,1,1,1,3,3,3,3,3,3,1,3,1],
    [1,1,3,3,3,3,3,3,3,1,1,1,3,3,3,3,3,3,3,1,1], 
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
]

x = 10 
y = 10
sum = 0
 
# FUNCTION FOR GRID CREATE GRAPHIC GAME

def gridToDraw() :
    global sum

    canvas.delete('all')

    for rowIndex in range(len(grid)):
        for columnIndex in range(len(grid[rowIndex])):
            arrayPos = grid[rowIndex][columnIndex]
            x1 = 50*columnIndex
            y1 = 50*rowIndex 
            x2 = x1 + 50    
            

            y2 = y1 + 50
            if arrayPos == WALL:
                canvas.create_rectangle(x1, y1+100, x2, y2+100, fill="#4d1a00",outline="orange")
            elif  arrayPos == PLAYER:
                players = canvas.create_image(x1+25,y1+120,image=player) 
            elif arrayPos == COIN :
                cion = canvas.create_image(x1+25,y1+125,image=coins) 
            elif arrayPos == ANAMY :
                monster = canvas.create_image(x1+25,y1+125,image=zombies) 
            elif arrayPos == GOLD :
                golds = canvas.create_image(x1+25,y1+125,image=gold) 
            
# SHOW SCORE 

def showScore():
    global condition

    myScore = "SCORE:"+str(sum)
    if not condition :
        canvas.create_rectangle(200,300,850,800,fill="gray",outline="green")
        canvas.create_text(525,500,fill="yellow",font="Times 20 italic bold",text="GAME OVER")
        canvas.create_text(525,550,fill="yellow",font="Times 20 italic bold",text="FINAL "+myScore) 
    else:
        canvas.create_text(200,50,fill="yellow",font="Times 20 italic bold",text=myScore)
        if sum == 636 :
            canvas.create_rectangle(200,300,850,800,fill="gray",outline="green")
            canvas.create_text(525,500,fill="yellow",font="Times 20 italic bold",text="YOU WIN")
            canvas.create_text(525,550,fill="yellow",font="Times 20 italic bold",text="FINAL "+myScore)

# FIND THE PLAYER IN GRID FOR CAN MOVE OR NOT

def findPlayer(grid) :
    for rows in range(len(grid)):
        for cols in range(len(grid[rows])):
            if grid[rows][cols] == PLAYER:
                position = [rows, cols]
    return position

# PLAYER FOR MOVE RIGHT LEFT UP DOWN

def move(direction):
    global sum, condition

    player = findPlayer(grid)
    playerRow = player[0]
    playerColumn = player[1]

    # COMPUTE THE NEXT POSSITION 

    if condition :
        if direction == 'right':
            nextRow = playerRow
            nextColumn = playerColumn + 1

        elif direction == 'left':
            nextRow = playerRow
            nextColumn = playerColumn - 1

        elif direction == 'up':
            nextRow = playerRow -1
            nextColumn = playerColumn 

        elif direction == 'down':
            nextRow = playerRow +1
            nextColumn = playerColumn 
        
        if  grid[nextRow][nextColumn] != WALL :

            # MANAGE THE COINS

            if grid[nextRow][nextColumn] == COIN:
                # winsound.PlaySound("test.wav",winsound.SND_sound/coin2.wav)
                sum += COIN
            elif grid[nextRow][nextColumn] == GOLD:
                sum += GOLD

            # MANAGE THE ANAMY 

            if grid[nextRow][nextColumn] == ANAMY:
                condition = False
            else:
                
            # MANGE PLAYER

                grid[playerRow][playerColumn] = EMPTY
                grid[nextRow][nextColumn] = PLAYER

    #   CALL GRID TO DRAW AND SHOWSCORE

    gridToDraw()
    showScore()

# MOVE ANAMY IN THE GRID



# CALL FUNCTION FOR MOVE THE PLAYER

def moveRight(event):
    move('right')

def moveLeft(event):
    move('left')

def moveDown(event):
    move('down')

def moveUp(event):
    move('up')

# IMAGES FOR PLAYER , COIN AND MONSTER

player = tk.PhotoImage(file="picture/player.png")
zombies = tk.PhotoImage(file="picture/monster.png")
coins = tk.PhotoImage(file="picture/coin.png")
gold = tk.PhotoImage(file="picture/gold_1.png")

# SOUN FOR GAME 



# CALL FUCTION FOR CAN MOVE THE PLAYER AND MONSTER IN GRID

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Down>", moveDown)
root.bind("<Up>", moveUp)

gridToDraw()

canvas.pack(expand=True, fill="both")
root.mainloop()
  