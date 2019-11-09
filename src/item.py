# -*- coding: utf-8 -*-

import pygame
from src.common import getSetting
from src.style import style

class Item():
    def __init__(self, settings):
        self.x = 0
        self.y = 0
        self.cellSize = getSetting(settings, "cellSize", 10)
        self.cellSize2 = int(self.cellSize / 2)
        self.eatenUpCount = 0

    def draw(self, screen):
        pygame.draw.circle(screen,
                           style.ItemColor,
                           (self.x * self.cellSize + self.cellSize2
                           ,self.y * self.cellSize + self.cellSize2)
                           ,self.cellSize2)

    def isEaten(self, x, y):
        result = (x == self.x) and (y == self.y)
        if result:
            self.eatenUpCount = self.eatenUpCount + 1
        return result
