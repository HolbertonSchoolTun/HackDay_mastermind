#!/usr/bin/python3
""
import pygame
from mastermind import Mastermind
from singleplayer import SinglePlayer
from pygame.locals import *

def start_game():
    result = [0,0,0,0]

    LEFT = 1
    RIGHT = 3
    COLOR = 0
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 204, 0)
    RED = (255, 0, 0)
    BLUE = (0, 102, 204)
    YELLOW = (255, 255, 0)
    PURPLE = (153, 0, 153)
    ORANGE = (255, 128, 0)
    COLORS = {0: WHITE, 1: GREEN, 2: RED, 3: BLUE,4:YELLOW, 5:PURPLE, 6:ORANGE}
    rows = 12
    columns = 6
    turn = 11
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 40
    HEIGHT = 40
    
    # This sets the margin between each cell
    MARGIN = 5
    
    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(rows):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(columns):
            grid[row].append(0)  # Append a cell
    
    # Initialize pygame
    pygame.init()
    
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [300, 600]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # Set title of screen
    pygame.display.set_caption("Mastermind")
    
    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    m = SinglePlayer()
   
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates        
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if turn == row and column < 4:
                    COLOR += 1
                    COLOR = COLOR%7
                    grid[row][column] = COLOR
                    result[column] = COLOR
                elif column < 10 and row == 12 and column > 4:
                    turn -= 1
                    m.Player_Input(result)
                    m.compare()
                    #print(result)
                    #print(m.playerinput)
                    print(m.objective)
                #print(COLOR)
                print("Click ", pos, "Grid coordinates: ", row, column)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                if turn == row:

                    COLOR -= 1
                    COLOR = COLOR % 7
                    grid[row][column] = COLOR
                    result[column] = COLOR
                #print(COLOR)
                print("Click ", pos, "Grid coordinates: ", row, column)

    
        # Set the screen background
        screen.fill(BLACK)
    
        # Draw the grid
        for row in range(rows):
            for column in range(columns):
                if column < 4:
                    color = WHITE
                    color = COLORS[grid[row][column]]
                    pygame.draw.rect(screen,
                                    color,
                                    [(MARGIN + WIDTH) * column + MARGIN,
                                    (MARGIN + HEIGHT) * row + MARGIN,
                                    WIDTH,
                                    HEIGHT])
        s = 500
        pygame.draw.rect(screen,RED,(200,550,80,40))

        for i in range(rows):
            pygame.draw.rect(screen,WHITE,(200,s,80,40))
            a = 220
            if i == turn:
                if len(m.result) != 0:
                    for j in range(m.result[0]):
                        pygame.draw.circle(screen, RED, (a, s+ 10), 5, 0)
                    for k in range(m.result[1]):
                        pygame.draw.circle(screen, GREEN, (a, s+ 10), 5, 0)
                        a += 10
            s -= 45
        #print(b)
        # Limit to 60 frames per second
        clock.tick(120)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()