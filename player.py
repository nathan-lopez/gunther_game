import pygame
# from game import Game

pygame.init()

# créartion de la classe player


class Player(pygame.sprite.Sprite):
    def __init__(self, cote, chemin):
        super().__init__()
        self.is_life = True
        self.image = pygame.image.load(chemin)
        self.cote = cote
        self.image = pygame.transform.scale(self.image, (69, 69))
        self.rect = self.image.get_rect()
        # instancier la classe move

    def is_present(self, x, y):
        if self.rect.x == x and self.rect.y == y:
            return True
        else:
            return False
