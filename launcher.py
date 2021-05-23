from tkinter import *
from tkinter.messagebox import askokcancel

class Launcher:
    def __init__(self, tampon):
        self.tampon = tampon
        self.run = False
        # self.nb_fen = self.main.compte
        self.windows()

    def change_run(self):
        self.run = True

    def windows(self):
        if self.run:
            self.root = Tk()
            self.root.geometry("460x350")
            self.root.minsize(460, 350)
            self.root.maxsize(460, 350)
            self.root.config(background='white')
            self.root.title("Launcher")
            self.rep = None
            self.photo = PhotoImage(file="assets/image.png").zoom(20).subsample(22)
            self.constructeur(self.root, self.photo)
            self.fermeture()
            # verifier le nombre de fois que la fenetre a été appelé

    def play(self):
        self.root.destroy()
        self.tampon.launche_pygame()

    def constructeur(self, root, photo):
        largeur = 350
        longeur = 350
        fram = Frame(root, bg="black", relief=SUNKEN)
        can = Canvas(root, width=largeur, height=longeur, bg='white')
        can.create_image(largeur / 2, longeur / 2, image=photo)
        can.grid(row=1, column=1)
        boutton = Button(fram, text="Jouer", command=self.play)
        boutton.grid(row=1, pady=45)
        boutton3 = Button(fram, text="apropos")
        boutton3.grid(row=2, pady=45)
        boutton2 = Button(fram, text='Quitter ', command=self.com_ok)
        boutton2.grid(row=3, pady=45)
        # construction du frame dans lequel on mettra nos bouttons
        fram.grid(row=1, column=2, padx=10)

    def com_ok(self):
        self.rep = askokcancel("confirmer la fermeture ", "voulez vous quitter le jeu ?")
        if self.rep:
            self.tampon.fermeture = False
            self.root.quit()

    def fermeture(self):
        self.root.protocol("WM_DELETE_WINDOW", self.com_ok)
        self.root.mainloop()