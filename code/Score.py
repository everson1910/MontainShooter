import pygame


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self):
        pass

    def show_score(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(surface=self.surf, dest=self.rect)
        while True:

            pygame.display.flip()
            pass