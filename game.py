import pygame
from player import Player
from fonction_du_jeu import Function


pygame.init()


class Game:
    def __init__(self):
        # variable qui va nous dire si l'user lance le jeu
        self.on_joue = False
        self.function = Function()

    def start(self):
        # en change cette variable le jeu demande
        self.on_joue = True

    def c_partie(self, screen):
        # on affiche le premier groupe de joueur
        for i in self.function.planjoeur(side="N"):
            screen.blit(Player("N", "assets/coca.png").image, self.function.dicofinal()[i])
        # on affiche le deuxieme groupe de joueur
        for ii in self.function.planjoeur(side="S"):
            screen.blit(Player("S", "assets/Fanta.jpg").image, self.function.dicofinal()[ii])
