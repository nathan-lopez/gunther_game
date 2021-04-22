import pygame


pygame.init()

# créartion de la classe player


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.is_life = True
        self.image = pygame.image.load("assets/coca.png")
        self.image = pygame.transform.scale(self.image, (69, 69))
        self.rect = self.image.get_rect()


# seconde classe player pour notre deuxieme joueur
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.is_life = True
        self.image = pygame.image.load("assets/Fanta.jpg")
        self.image = pygame.transform.scale(self.image, (69, 69))
        self.rect = self.image.get_rect()
