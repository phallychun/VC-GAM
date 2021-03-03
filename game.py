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
gameNotOver = True

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
choiceToMoveAnamy = []
 
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
    global gameNotOver
    myScore = "SCORE:"+str(sum)
    if not gameNotOver :
        canvas.create_rectangle(200,300,850,800,fill="gray")
        canvas.create_text(525,500,fill="yellow",font="Times 20 italic bold",text="GAME OVER")
        canvas.create_text(525,550,fill="yellow",font="Times 20 italic bold",text="FINAL "+myScore) 
    else:
        canvas.create_text(200,50,fill="yellow",font="Times 20 italic bold",text=myScore)
       
        if sum >= 700 and sum <= 780:
            canvas.create_image(510,550,image=win) 
            canvas.create_text(525,500,fill="white",font="Times 20 italic bold",text="YOU WIN")
            canvas.create_text(525,550,fill="white",font="Times 20 italic bold",text="FINAL "+myScore)
            gameNotOver = False

# FIND THE PLAYER IN GRID FOR CAN MOVE OR NOT

def findPlayer(grid) :
    for rows in range(len(grid)):
        for cols in range(len(grid[rows])):
            if grid[rows][cols] == PLAYER:
                position = [rows, cols]
    return position

# PLAYER FOR MOVE RIGHT LEFT UP DOWN

def move(direction):
    global sum, gameNotOver

    player = findPlayer(grid)
    playerRow = player[0]
    playerColumn = player[1]

    # COMPUTE THE NEXT POSSITION 

    if gameNotOver :
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
                sum += 5
            elif grid[nextRow][nextColumn] == GOLD:
                sum += 10

            # MANAGE THE ANAMY 
            if grid[nextRow][nextColumn] == ANAMY:
                gameNotOver = False
            else:
            # MANGE PLAYER
                grid[playerRow][playerColumn] = EMPTY
                grid[nextRow][nextColumn] = PLAYER

    #   CALL GRID TO DRAW AND SHOWSCORE

    gridToDraw()
    showScore()

#  FUNCTION FOR MOVE THE ENEMMIES

def getAllEnnemiesPositions(grid):
    ennemiesPOsitions = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ANAMY:
                ennemiesPOsitions.append([row,col])

    return ennemiesPOsitions

def canMoveAnamy(grid,row,col):
    global choiceToMoveAnamy
    choiceToMoveAnamy = []
    if grid[row][col-1] != WALL and grid[row][col-1] != ANAMY:
        choiceToMoveAnamy.append('left')
    if grid[row][col+1] != WALL and grid[row][col+1] != ANAMY:
        choiceToMoveAnamy.append('right')
    if grid[row-1][col] != WALL and grid[row-1][col] != ANAMY:
        choiceToMoveAnamy.append('up')
    if grid[row+1][col] != WALL and grid[row+1][col] != ANAMY:
        choiceToMoveAnamy.append('down')
    return choiceToMoveAnamy

def moveAllEnnemies():
    global choiceToMoveAnamy,gameNotOver
    for ennemy in getAllEnnemiesPositions(grid) :
        enemyRow = ennemy[0]
        ennemyColumn = ennemy[1]
        placeToMove = canMoveAnamy(grid, enemyRow, ennemyColumn)
        if len(placeToMove)> 0:
            randomAnamy = random.choice(placeToMove)
            if  gameNotOver :
                if randomAnamy == 'right':
                    if grid[enemyRow][ennemyColumn+1] != WALL:
                        if grid[enemyRow][ennemyColumn+1] == PLAYER:
                            gameNotOver = False
                        elif grid[enemyRow][ennemyColumn+1] == GOLD:
                            grid[enemyRow][ennemyColumn+1] = ANAMY
                            grid[enemyRow][ennemyColumn] = GOLD
                        else:
                            grid[enemyRow][ennemyColumn+1] = ANAMY
                            grid[enemyRow][ennemyColumn] = COIN
                elif randomAnamy == 'left':
                    if grid[enemyRow][ennemyColumn-1] != WALL:
                        if grid[enemyRow][ennemyColumn-1] == PLAYER:
                            gameNotOver = False
                        elif grid[enemyRow][ennemyColumn-1] == GOLD:
                            grid[enemyRow][ennemyColumn-1] = ANAMY
                            grid[enemyRow][ennemyColumn] = GOLD
                        else:
                            grid[enemyRow][ennemyColumn-1] = ANAMY
                            grid[enemyRow][ennemyColumn] = COIN
                elif randomAnamy == 'down':
                    if grid[enemyRow+1][ennemyColumn] != WALL:
                        if grid[enemyRow+1][ennemyColumn] == PLAYER:
                            gameNotOver = False
                        elif grid[enemyRow+1][ennemyColumn] == GOLD:
                            grid[enemyRow+1][ennemyColumn] = ANAMY
                            grid[enemyRow][ennemyColumn] = GOLD
                        else:
                            grid[enemyRow+1][ennemyColumn] = ANAMY
                            grid[enemyRow][ennemyColumn] = COIN
                elif randomAnamy == 'up':
                    if grid[enemyRow-1][ennemyColumn] != WALL:
                        if grid[enemyRow-1][ennemyColumn] == PLAYER:
                            gameNotOver = False
                        elif grid[enemyRow-1][ennemyColumn] == GOLD:
                            grid[enemyRow-1][ennemyColumn] = ANAMY
                            grid[enemyRow][ennemyColumn] = GOLD
                        else:
                            grid[enemyRow-1][ennemyColumn] = ANAMY
                            grid[enemyRow][ennemyColumn] = COIN




        # decide here to moeve  ennmy

    canvas.delete('all')
    gridToDraw()
    canvas.after(500,lambda: moveAllEnnemies())
    showScore()



# CALL FUNCTION FOR MOVE THE PLAYER

def moveRight(event):
    move('right')

def moveLeft(event):
    move('left')

def moveDown(event):
    move('down')

def moveUp(event):
    move('up')

#CALL FUNCTION FRO MOVE THE ANAMY



# IMAGES FOR PLAYER , COIN AND MONSTER

player = tk.PhotoImage(file="picture/player.png")
zombies = tk.PhotoImage(file="picture/monster.png")
coins = tk.PhotoImage(file="picture/coin.png")
gold = tk.PhotoImage(file="picture/gold_1.png")
win = tk.PhotoImage(file="picture/congratulation.gif") 

# SOUN FOR GAME 



# CALL FUCTION FOR CAN MOVE THE PLAYER AND MONSTER IN GRID

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Down>", moveDown)
root.bind("<Up>", moveUp)


gridToDraw()
moveAllEnnemies()
showScore()

# staRT OT MOVE EENEMIES

canvas.pack(expand=True, fill="both")
root.mainloop()
  