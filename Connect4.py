#CONNECT FOUR GAME

#inporting libraries
from pygame import *
from numpy import *
from math import *

def game_board():
#creating game board in shell using numpy zeros to make array (a kind of matrix)
    create = zeros((6,7))
    return create 


def valid_loc(board, select):
        return board[5][select] == 0 #checking if the bottom part of the grid empty
    

#the following function returns r if the that r row from the selected column is empty
def get_next(board, select):
    for r in range(6):
        if board[r][select] == 0:
            return r
        

#the r returned from the above function will be used in the following function as the row
def drop(board, row, select, item):
    board[row][select] = item #it contains the board when it equals to something other than 0
    

def winning(board, item):
    #horizontal win
    for c in range(4): #from 7 columns, only 4 will be used
        for r in range(6):
            if board[r][c] == item and board[r][c+1] == item and board[r][c+2] == item and board[r][c+3] == item:
                return True
    #vertical win
    for r in range(4): #from 6 columns, only 4 will be used
        for c in range(7):
            if board[r][c] == item and board[r+1][c] == item and board[r+2][c] == item and board[r+3][c] == item:
                return True
    #progressing diagonal win 
    for c in range(4):
        for r in range(3):
            if board[r][c] == item and board[r+1][c+1] == item and board[r+2][c+2] == item and board[r+3][c+3] == item:
                return True
    #regressing diagonal win
    for c in range(4):
        for r in range (3, 6):
            if board[r][c] == item and board[r-1][c+1] == item and board[r-2][c+2] == item and board[r-3][c+3] == item:
                return True

              
def run():
    global game_on, player, board
    txt = font.SysFont('arial', 60)
    while game_on: #mainloop
        for e in event.get(): #event handling
            if e.type == QUIT: #to quit the pygame window if
                game_on = False #breaks out of the while loop
                quit()
            if e.type == MOUSEBUTTONDOWN: #when mouse button is clicked
                #ask for player 1 input
                if player == 0:
                    xpos = e.pos[0] #returns the x coordinate
                    select = int(floor(xpos/80)) #chooses the column to put circles
                    if valid_loc(board, select):
                        row = get_next(board, select)
                        #put the item 1 into the selected column
                        drop(board, row, select, 1)
                        #draws circle every turn
                        for r in range(6):
                            for c in range(7):
                                if board[r][c] == 1:
                                    draw.circle(screen, (255, 0, 0), (int(c*80+40), width-(int(r*80+40))), 37)
                                display.update()
                        #if all items in winning is 1
                        if winning(board, 1):
                            notif = txt.render('Red Wins!!', True, (255, 0, 0))
                            #displays the text above into the pygame diaplay window
                            screen.blit(notif, (170,5)) 
                    display.update() #updates screen)

                    
                #ask for player 2
                else:
                    xpos = e.pos[0]
                    select = int(floor(xpos/80))
                    if valid_loc(board, select):
                        row = get_next(board, select)
                        drop(board, row, select, 2)
                        for r in range(6):
                            for c in range(7):
                                if board[r][c] == 2:
                                    draw.circle(screen, (255,255, 0), (int(c*80+40), width-(int(r*80+40))), 37)
                                display.update()
                        if winning(board, 2):
                            notif = txt.render('Yellow Wins!!', True, (255, 255, 0))
                            screen.blit(notif, (145,5))
                    display.update()


                #to change player's turns
                player += 1
                player %= 2
                print(flip(board, 0)) #numpy.flip, to make it start from the bottom
                    

#the following function draws grid on pygame display window
def draw_grid(surface, width, height):
    square_size = width//7 #7, including the blank space at the top
    x = 0
    y = 0
    for c in range(7):
        x += square_size
        y += square_size
        #draws horizontal lines
        draw.line(screen, (255, 255, 255), (x,80), (x,width))
        #draws vertical lines
        draw.line(screen, (255, 255, 255), (0,y), (height,y))
    display.update()


#main function
def main():
    global width, height, screen, board, game_on, player
    #constructions
    board = game_board()
    print(flip(board,0))
    game_on = True
    player = 0
    init() #initializes all imported pygame module
    width = 560
    height = 560
    screen = display.set_mode((width, height)) #set pygame display window
    display.set_caption('CONNECT 4') #add title to pygame display window
    draw_grid(screen, width, height) #draws grid
    run() #calls the run function


#calls the main function
main()
