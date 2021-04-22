import pygame
from game import Game


pygame.init()
class Move:
    def __init__(self):
        self.game = Game()
        self.pas = 70
        self.hand = "N"

    def move_right(self, hand):
        print("on bouge!")
        #   if hand == "N":
        #   self.game.player1.rect =
