#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

    #def run(self, ): (CÓDIGO DA AULA QUE ESTAVA DANDO ERRO DA JANELA POR CAUSA DO RUN NO 1° LEVEL)
        #while True:
            #for ent in self.entity_list:
               # self.window.blit(source=ent.surf, dest=ent.rect)
            #pygame.display.flip()
            #pass

    # CÓDIGO DO CHAT
    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # sai do nível e volta pro menu

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
            clock.tick(60)