# -*- coding: utf-8 -*-

import pygame
from src.common import getSetting, Direction
from src.style import style

class Snake():
    def __init__(self, settings, x, y):
        self.x = x
        self.y = y
        self.cellSize = getSetting(settings, "cellSize", 10)
        self.direction = Direction.Up
        self.body = []
        length = getSetting(settings, "snakeLength", 3)
        for i in range(0, length):
            self.body.append((self.x, self.y))

    def draw(self, screen):
        for pos in self.body:
            pygame.draw.rect(screen,
                         style.SnakeTailColor,
                         (pos[0] * self.cellSize
                         ,pos[1] * self.cellSize
                         ,self.cellSize
                         ,self.cellSize))

    def setDirection(self, direction):
        if direction == None:
            return
        if self.direction == Direction.Down and direction == Direction.Up:
            return
        if self.direction == Direction.Right and direction == Direction.Left:
            return
        if self.direction == Direction.Up and direction == Direction.Down:
            return
        if self.direction == Direction.Left and direction == Direction.Right:
            return
        self.direction = direction

    def moveHead(self, x, y, isItemEaten):
        self.body.insert(0, (x, y))
        if not isItemEaten:
            self.body.pop()
        self.x = x
        self.y = y

    def isContains(self, x, y):
        return self.body.__contains__((x, y))
