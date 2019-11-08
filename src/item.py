# -*- coding: utf-8 -*-

import pygame
from src.common import getSetting

class Item():
    def __init__(self, settings):
        self.x = 0
        self.y = 0
        self.cellSize = getSetting(settings, "cellSize", 10)
        self.cellSize2 = int(self.cellSize / 2)
        self.eatenUpCount = 0

    def draw(self, screen):
        pygame.draw.circle(screen,
                         (64, 64, 128),
                         (self.x * self.cellSize + self.cellSize2
                         ,self.y * self.cellSize + self.cellSize2)
                         ,self.cellSize2)
