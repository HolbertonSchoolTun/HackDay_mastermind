#!/usr/bin/python3
"""
"""
import pygame
import pygame_menu
from main import start_game


class Game():
    pygame.init()
    surface = pygame.display.set_mode((450, 600))

    def set_difficulty(value, difficulty):
        if value == 1:
            return(1)
        else:
            return (2)

    def start_the_game():
        # Do the job here !
        start_game()

    def Play_Mode(mode, value):
        pass
    pygame.display.set_caption("Mastermind")
    menu = pygame_menu.Menu(600, 450, 'MasterMind',
                        theme=pygame_menu.themes.THEME_DARK)
    menu.add_selector('Difficulty : ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add_selector('Play Mode : ', [('Single Player', 1), ('Two Players', 2)], onchange=Play_Mode)
    menu.add_button('Play', start_the_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)