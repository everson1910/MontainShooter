#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.timeout = 20000 #20segundos

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

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            clock.tick(30)

            self.level_text( 14,  f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (75, 5))
            self.level_text( 14,  f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (30, WIN_HEIGHT - 35))
            self.level_text( 14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (50, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Tempus Sans ITC", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

