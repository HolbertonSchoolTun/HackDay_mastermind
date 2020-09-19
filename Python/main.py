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
    WIDTH = 40
    HEIGHT = 40
    
    MARGIN = 5
    

    grid = []
    for row in range(rows):

        grid.append([])
        for column in range(columns):
            grid[row].append(0)
    
    pygame.init()
    
    WINDOW_SIZE = [300, 600]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    pygame.display.set_caption("Mastermind")
    
    done = False
    
    clock = pygame.time.Clock()
    m = SinglePlayer()
   
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                pos = pygame.mouse.get_pos()
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
                    print(m.objective)
                print("Click ", pos, "Grid coordinates: ", row, column)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if turn == row:

                    COLOR -= 1
                    COLOR = COLOR % 7
                    grid[row][column] = COLOR
                    result[column] = COLOR
                print("Click ", pos, "Grid coordinates: ", row, column)

    
        screen.fill(BLACK)
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
        clock.tick(120)
        pygame.display.flip()

    pygame.quit()