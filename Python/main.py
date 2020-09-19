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
    BLACK = (40, 41, 36)
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
    WINDOW_SIZE = [450, 600]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    pygame.display.set_caption("Mastermind")
    
    done = False
    font = pygame.font.Font('freesansbold.ttf', 32)
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    font3 = pygame.font.Font('freesansbold.ttf', 14)

    image = pygame.image.load(r'/home/achref/Desktop/azer/HackDay_mastermind/Python/unnamed-2.png')
    image = pygame.transform.scale(image, (100, 100))

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
                    print('ok')
                    if 0 not in result:
                        turn -= 1
                        m.Player_Input(result)
                        m.compare()
                        result = [0,0,0,0]
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if turn == row:
                    COLOR -= 1
                    COLOR = COLOR % 7
                    grid[row][column] = COLOR
                    result[column] = COLOR
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
        pygame.draw.rect(screen,(255,90,120),(200,550,80,40))

        for i in range(rows):
            pygame.draw.rect(screen,WHITE,(200,s,80,40))
            a = 225
            if len(m.result) != 0:
                for j in range(m.result[0]):
                    pygame.draw.circle(screen, YELLOW, (a, s+ 20), 5, 0)
                    a += 10
                for k in range(m.result[1]):
                    pygame.draw.circle(screen, GREEN, (a, s+ 20), 5, 0)
                    a += 10
                for p in range(sum(m.result), 4):
                    pygame.draw.circle(screen, RED, (a, s+ 20), 5, 0)
                    a += 10
            s -= 45
        text = font.render("turn :{}".format(-(turn - 12)), True, WHITE)
        text2 = font2.render("Check", True, WHITE)
        text3 = font3.render("Game rules :", True, WHITE)
        text4 = font3.render("guess the pattern", True, WHITE)
        text5 = font3.render("both order and color", True, WHITE)
        text6 = font3.render("wrong position", True, WHITE)
        pygame.draw.circle(screen, YELLOW, (300, 320), 5, 0)
        text7 = font3.render("correct position", True, WHITE)
        pygame.draw.circle(screen, GREEN, (300, 350), 5, 0)
        text8 = font3.render("wrong color", True, WHITE)
        pygame.draw.circle(screen, RED, (300, 380), 5, 0)


        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect3 = text3.get_rect()
        textRect4 = text4.get_rect()
        textRect5 = text5.get_rect()
        textRect6 = text6.get_rect()
        textRect7 = text7.get_rect()
        textRect8 = text8.get_rect()

        textRect.center = (100 ,570)
        textRect2.center = (240 ,570)
        textRect3.center = (360 ,190)
        textRect4.center = (360 ,220)
        textRect5.center = (365 ,250)
        textRect6.center = (365 ,320)
        textRect7.center = (365 ,350)
        textRect8.center = (365 ,380)


        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)
        screen.blit(text5, textRect5)
        screen.blit(text6, textRect6)
        screen.blit(text7, textRect7)
        screen.blit(text8, textRect8)

        screen.blit(image, (320, 30)) 
        pygame.display.update()
        pygame.display.flip()


    pygame.quit()