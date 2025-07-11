#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Level import Level
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                result = level.run()
                if result == "GAME_OVER":
                    continue
                if result == "NEXT_LEVEL":
                    level = Level(self.window, 'Level2', menu_return)
                    result = level.run()
                    if result == "GAME_OVER":
                        continue

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                continue

        # COD DO CHAT PARA PARAR DE ENTRAR NO LEVEL 1 AO CLICAR EM QUALQUER LEVEL
        # if menu_return == MENU_OPTION[0]:  # NEW GAME 1P
        #   level = Level(self.window, 'Level1', menu_return)
        #  level.run()
        # elif menu_return == MENU_OPTION[1]:  # NEW GAME 2P - COOPERATIVE
        #   level = Level(self.window, 'Level2', menu_return)
        #  level.run()
        # elif menu_return == MENU_OPTION[2]:  # NEW GAME 2P - COMPETITIVE
        #   level = Level(self.window, 'Level3', menu_return)
        # level.run()
