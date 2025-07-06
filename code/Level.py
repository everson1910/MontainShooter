#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from random import choice

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_BLUE, C_MARINE
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    #def run(self, ): (CÓDIGO DA AULA QUE ESTAVA DANDO ERRO DA JANELA POR CAUSA DO RUN NO 1° LEVEL)
        #while True:
            #for ent in self.entity_list:
               # self.window.blit(source=ent.surf, dest=ent.rect)
            #pygame.display.flip()
            #pass

    # CÓDIGO DO CHAT
    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # sai do nível e volta pro menu
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14,  f'Player1 - Health: {ent.health} | Score: {ent.score}', C_BLUE, (95, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health}| Score: {ent.score}', C_MARINE, (95, 45))
            clock.tick(30)

            self.level_text(14,  f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (75, 5))
            self.level_text(14,  f'fps: {clock.get_fps() :.0f}', C_WHITE, (30, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (50, WIN_HEIGHT - 20))
            pygame.display.flip()
            #Collision
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Tempus Sans ITC", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

