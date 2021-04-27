import pygame
from game import Game
from math import ceil

pygame.init()


# classe principale du jeu
class MainGame:
    def __init__(self):
        self.game = Game()
        # variable de debut de jeu
        self.running = True

    def run(self):
        # enerer la fenetre du jeu, son titre, sa dimension en hauteur et largeur
        pygame.display.set_caption("Gunther_game")
        # ### constructon de la fenetre ####
        screen = pygame.display.set_mode((1080, 720))
        # j'importe l'arriere plan et je le stocke dans la variable bg1
        # le deux arriere plan
        bg = pygame.image.load("assets/bg1.jpg")
        bg2 = pygame.image.load("assets/damier.png")
        # refaire l'image le modifier car il est trop gand
        bg2 = pygame.transform.scale(bg2, (700, 700))
        bg2_rect = bg2.get_rect()
        bg2_rect.x = ceil(screen.get_width()/6)         # reoganisation de l'affichage
        bg2_rect.y = ceil(screen.get_width()/(screen.get_width()/7))
        # ###construction de la page d'acceuil ####
        # importation de la bannier
        banner = pygame.image.load("assets/ban.jpg")
        banner = pygame.transform.scale(banner, (600, 450))               # reoganisation de l'affichage
        banner_rect = banner.get_rect()
        banner_rect.x = ceil(screen.get_width() / 4 - 30)
        #  importer le bouton
        play_button = pygame.image.load("assets/button.png")
        play_button = pygame.transform.scale(play_button, (450, 200))
        play_button_rect = play_button.get_rect()
        play_button_rect.x = ceil(screen.get_width() / 3.3 - 12)
        play_button_rect.y = ceil(screen.get_height() / 2 - 180)
        # lançons la boucle
        self.boucle_du_jeu(screen, bg, bg2, bg2_rect, banner, banner_rect, play_button, play_button_rect)
        return bg2_rect

    def boucle_du_jeu(self, screen, bg, bg2, bg2_rect, banner, banner_rect, play_button, play_button_rect):
        while self.running:
            # je vais appliquer l'arriere plan du jeu
            screen.blit(bg, (25, -100))
            # je verifie si le joueur lance la partie, si oui , on lance le jeu
            if self.game.on_joue:
                screen.blit(bg2, (bg2_rect.x, bg2_rect.y))
                self.game.c_partie(screen)            # chargement de la partie de game qui s'occupe du jeu

            # si non on affiche l'ecran d'acceuil
            else:
                screen.blit(banner, (banner_rect.x, 40))
                screen.blit(play_button, (play_button_rect.x, play_button_rect.y))

            # mettre à jour la fenetre
            pygame.display.flip()
            # recuperation de different evenement de notre jeu
            for event in pygame.event.get():
                # evenement 1 : si l'unitisateur ferme la fenetre X
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                # evenement 2 : si l'utilisateur fait un clique
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # verfifions si il a cliquer sur notre boutton
                    if play_button_rect.collidepoint(event.pos):
                        # si oui , on met le jeu sur start
                        self.game.start()