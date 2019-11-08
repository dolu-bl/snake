# -*- coding: utf-8 -*-

import pygame
import random
from src.common import getSetting, Direction
from src.snake import Snake
from src.item import Item

class Board():
    def __init__(self, settings):
        self.boardWidth = getSetting(settings, "boardWidth", 10)
        self.boardHeight = getSetting(settings, "boardHeight", 10)
        self.cellSize = getSetting(settings, "cellSize", 10)
        self.snake = Snake(settings,
                           self.boardWidth / 2,
                           self.boardHeight / 2)
        self.isDead = False
        self.item = Item(settings)
        self.reinitItem()

    def draw(self, screen):
        self.move()
        screen.fill((0,0,0))
        for row in range(0, self.boardWidth):
            for column in range(0, self.boardHeight):
                x = row * self.cellSize
                y = column * self.cellSize
                color = (64, 64, 64)
                if self.isDead:
                    color = (128, 32, 32)
                pygame.draw.rect(screen,
                                 color,
                                 (x, y, self.cellSize, self.cellSize),
                                 1)
        self.item.draw(screen)
        self.snake.draw(screen)

    def move(self):
        if self.snake.direction == Direction.Up:
            self.tryMove(self.snake.x, self.snake.y - 1)
        elif self.snake.direction == Direction.Right:
            self.tryMove(self.snake.x + 1, self.snake.y)
        elif self.snake.direction == Direction.Down:
            self.tryMove(self.snake.x, self.snake.y + 1)
        elif self.snake.direction == Direction.Left:
            self.tryMove(self.snake.x - 1, self.snake.y)

    def tryMove(self, x, y):
        self.isDead = ((x < 0) or
                       (x >= self.boardWidth) or
                       (y < 0) or
                       (y >= self.boardHeight) or
                       self.snake.isContains(x, y))
        if self.isDead:
            return

        isItemEaten = (x == self.item.x) and (y == self.item.y)
        if isItemEaten:
            self.item.eatenUpCount = self.item.eatenUpCount + 1
            self.reinitItem()

        self.snake.moveHead(x, y, isItemEaten)

    def reinitItem(self):
        self.item.x = random.randint(0, self.boardWidth - 1)
        self.item.y = random.randint(0, self.boardHeight - 1)
