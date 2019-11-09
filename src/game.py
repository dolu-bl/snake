# -*- coding: utf-8 -*-

import pygame
from src.board import Board
from src.common import getSetting, Direction

class Game():
    def __init__(self, settings):
        self.screen = None
        self.clock = None
        self.isRunning = True
        self.fps = getSetting(settings, "fps", 30)
        self.speed = getSetting(settings, "speed", 1)
        self.board = Board(settings)
        width = getSetting(settings, "width",
                           self.board.boardWidth * self.board.cellSize)
        height = getSetting(settings, "height",
                            self.board.boardHeight * self.board.cellSize)
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

    def run(self):
        drawCounter = 0
        newDirection = None
        while self.isRunning:
            self.clock.tick(self.fps)
            drawCounter = drawCounter + 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT : self.isRunning = False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE : self.isRunning = False
                    elif event.key == pygame.K_UP : newDirection = Direction.Up
                    elif event.key == pygame.K_RIGHT : newDirection = Direction.Right
                    elif event.key == pygame.K_DOWN : newDirection = Direction.Down
                    elif event.key == pygame.K_LEFT : newDirection = Direction.Left

            if drawCounter < int(self.fps / self.speed):
                continue

            drawCounter = 0
            self.board.snake.setDirection(newDirection)
            self.board.draw(self.screen)
            pygame.display.flip()
            self.printInfo()

            if self.board.isDead:
                self.isRunning = False

        pygame.quit()

    def printInfo(self):
        pygame.display.set_caption(
            "Snake score: " +
            str(self.board.item.eatenUpCount) +
            " speed: " +
            str(self.speed))
