# -*- coding: utf-8 -*-
from src.game import Game

def main():
    game = Game({ "cellSize" : 30
                , "boardWidth" : 30
                , "boardHeight" : 20
                , "speed" : 2
                , "snakeLength" : 4
                })
    game.run()

if __name__ == "__main__":
    main()
