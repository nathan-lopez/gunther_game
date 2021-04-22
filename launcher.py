class Launcher:
    def __init__(self):
        self.main = MainGame()
        # #### initialisation de la fenetre tkinter #####
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

    def play(self):
        # fermer la fenetre tkinter si pygame est lancer
        self.root.destroy()
        self.main.run()

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

    def launcher_game(self):
        self.main = MainGame()
        self.main.run()

    def com_ok(self):
        self.rep = askokcancel("confirmer la fermeture ", "voulez vous quitter le jeu ?")
        if self.rep:
            self.root.quit()

    def fermeture(self):
        self.root.protocol("WM_DELETE_WINDOW", self.com_ok)
        self.root.mainloop()


# prorgramme principal
if __name__ == '__main__':
    from tkinter import *
    from tkinter.messagebox import askokcancel
    from main import MainGame
    Gunther_game = Launcher()
