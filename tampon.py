from launcher import Launcher
from main import MainGame

class Tampon:
    def __init__(self):
        # se chargera de faire la laison entre tkinter et pygame
        self.tkinter_w = Launcher(self)
        self.pygame_w = MainGame(self)
        self.fermeture = True
        # tampon s'initialise en lançant tkinter

    def pygame_is_closed(self):
        return True

    def fermer_tkinter(self, root):
        root.quit()
    # lancer pygame
    def launche_pygame(self):
        self.pygame_w.run()

    # methode pour lancer notre jeu
    def start_game(self):
        # lancer tkinter
        self.tkinter_w.run = True
        self.tkinter_w.windows()
