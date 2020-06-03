import pygame


class Player():
    def __init__(self, hand):
        self.hand = hand

    def card(self, win, x, y, pos):
        playercard = pygame.transform.scale(pygame.image.load(f'Images/{self.hand[pos]}.png'), (150, 200))
        win.blit(playercard, (x, y))
