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

        if self.board.isDead:
            self.gameover()
        pygame.quit()

    def printInfo(self):
        pygame.display.set_caption(
            "Snake score: " +
            str(self.board.item.eatenUpCount) +
            " speed: " +
            str(self.speed))

    def gameover(self):
        x = self.board.boardWidth * self.board.cellSize / 2
        y = self.board.boardHeight * self.board.cellSize / 2

        overFont = pygame.font.SysFont('Arial', 60, True)
        overText = overFont.render('GAME OVER', True, (128, 128, 0), (64, 0, 0))
        overWidth2 = int(overText.get_width() / 2)
        overHeight2 = int(overText.get_height() / 2)
        self.screen.blit(overText, (x - overWidth2, y - overHeight2))

        moreFont = pygame.font.SysFont('Arial', 12)
        moreText = moreFont.render('Press Esc to quit', True, (128, 128, 128), (32, 32, 32))
        moreWidth2 = int(moreText.get_width() / 2)
        self.screen.blit(moreText, (x - moreWidth2, y + overHeight2))

        pygame.display.flip()

        escapePressed = False
        while not escapePressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    escapePressed = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    escapePressed = True
