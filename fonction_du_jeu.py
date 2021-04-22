import pygame
# from main import MainGame

pygame.init()
# ce que nousallons faire
# differents tableau qui vont nous permettre de referencier chaque cellules


class Function:
    def __init__(self):
        self.alpha_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.x1 = 180
        self.y1 = 7
        self.x = self.x1 + 700
        self.y = self.y1 + 700
        self.case_x, self.case_y = 0, 0
        self.dico = {}

    def array(self, alpha, number):
        tab = []
        for a in range(0, (len(alpha))):
            c = alpha[a]
            for bb in range(0, (len(number))):
                v = number[bb]
                chaine = c + str(v)
                tab.append(chaine)
        # retourne une suite de combinaisons alphaber + chiffres
        return tab

    def coordos(self):
        key_array = self.array(self.alpha_array, self.number_array)
        tabf = []
        while self.x1 < self.x:
            self.y1 = 7
            self.case_x = self.x1
            while self.y1 < self.y:
                self.case_y = self.y1
                tup = (self.case_x, self.case_y)
                tabf.append(tup)
                self.y1 += 70
            self.x1 += 70
        for kk in range(0, (len(key_array))):
            try:
                self.dico[key_array[kk]] = tabf[kk]
            except IndexError:
                pass
        # retourne toute les reference de chaque case sur le damier
        return self.dico

    def dicofinal(self):
        # retirer la zone dans la quelle le joeur ne jouerons pas
        dico = self.coordos()
        array_a = (
            "a1", "a3", "a5", "a7", "a9",
            "b2", "b4", "b6", "b8", "b10",
            "c1", "c3", "c5", "c7", "c9",
            "d2", "d4", "d6", "d8", "d10",
            "e1", "e3", "e5", "e7", "e9",
            "f2", "f4", "f6", "f8", "f10",
            "g1", "g3", "g5", "g7", "g9",
            "h2", "h4", "h6", "h8", "h10",
            "i1", "i3", "i5", "i7", "i9",
            "j2", "j4", "j6", "j8", "j10"
        )
        for i in array_a:
            if i in dico:
                del dico[i]
        # retourne un dictionnaire de reference( coordonées) de jeu où le joeur va joeur
        return dico

    # fonction qui nous permettra d'avoir le reference de depart de jeu de nos joeur
    # ainsi que l'intervale entre les deux camps

    def planjoeur(self, side="N"):
        player_A = [
                "a2", "a4", "b1", "b3"
                , "c2", "c4", "d1", "d3"
                , "e2", "e4", "f1", "f3"
                , "g2", "g4", "h1", "h3"
                , "i2", "i4", "j1", "j3"
        ]
        player_I = [
            "a6", "b5", "c6", "d5", "e6",
            "f5", "g6", "h5", "i6", "j5"
        ]
        player_B = [
            "a8", "a10", "b9", "b7"
            , "c8", "c10", "d9", "d7"
            , "e8", "e10", "f9", "f7"
            , "g8", "g10", "h9", "h7"
            , "i8", "i10", "j9", "j7"
        ]
        if side == "N":
            return player_A
        elif side == "S":
            return player_B
        elif side == "I":
            return player_I
