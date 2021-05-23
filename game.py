import pygame
from player import Player
from fonction_du_jeu import Function


pygame.init()


class Game:
    def __init__(self):
        # variable qui va nous dire si l'user lance le jeu
        self.on_joue = False
        self.function = Function()
        self.player1 = Player("N", "assets/coca.png")
        self.player2 = Player("S", "assets/Fanta.jpg")
        self.liste_rect = []


    def start(self):
        # en change cette variable le jeu demande
        self.on_joue = True

    def c_partie(self, screen):
        # on affiche le premier groupe de joueur
        # for i in self.function.planjoeur(side="N"):
        screen.blit(self.player1.image, self.function.dicofinal()["c2"])
        # on affiche le deuxieme groupe de joueur
       #  for ii in self.function.planjoeur(side="S"):
        screen.blit(self.player2.image, self.function.dicofinal()["d9"])


    def tab(self):
        # liste de tout le rectangle
        for iii in self.function.planjoeur(side="I"):
            self.liste_rect.append(pygame.Rect(self.function.dicofinal()[iii], (70, 70)))
        return self.liste_rect

