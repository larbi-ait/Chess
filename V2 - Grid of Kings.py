import pyxel
class Piece :
    def __init__(self, nom : str, x : int, y : int, EstBlanc : bool) :
        self.nom = nom
        self.x = x
        self.y = y
        self.EstBlanc = EstBlanc

class Grille :
    def __init__(self) :
        self.echiquier = self.creer_echiquier()
        self.Taille_Cellule = 16

    def creer_echiquier(self) :
        l =[]
        eph = [0,0,0,0,0,0,0,0]
        for i in range(8) :
            l.append(eph)
        return l

    def afficher_echiquier(self) :
        for i in self.echiquier :
            print(i, "\n")

    def dessiner_blanc_noir(self, ligne : int) :
        pyxel.rect(64 + 0*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 7)
        pyxel.rect(64 + 1*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 0)
        pyxel.rect(64 + 2*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 7)
        pyxel.rect(64 + 3*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 0)
        pyxel.rect(64 + 4*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 7)
        pyxel.rect(64 + 5*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 0)
        pyxel.rect(64 + 6*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 7)
        pyxel.rect(64 + 7*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 0)

    def dessiner_noir_blanc(self, ligne : int) :
        pyxel.rect(64 + 0*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 0)
        pyxel.rect(64 + 1*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 7)
        pyxel.rect(64 + 2*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 0)
        pyxel.rect(64 + 3*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 7)
        pyxel.rect(64 + 4*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 0)
        pyxel.rect(64 + 5*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 7)
        pyxel.rect(64 + 6*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 0)
        pyxel.rect(64 + 7*self.Taille_Cellule, 64 + ligne*self.Taille_Cellule, self.Taille_Cellule, self.Taille_Cellule, 7)

    def dessiner_grille(self) :
        for ligne in range(8):
            for colonne in range(8):
                if ligne % 2 == 0 :
                    self.dessiner_blanc_noir(ligne)
                else :
                    self.dessiner_noir_blanc(ligne)


class App:
    def __init__(self):
        self.plateau = Grille()
        pyxel.init(256, 256, title="Grid Of Kings")
        pyxel.run(self.update, self.draw)

    def dessiner_arriere_plan(self) :
        pyxel.rect(0, 0, 256, 256, 7)
        pyxel.rect(48, 48, 160, 160, 13)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.dessiner_arriere_plan()
        self.plateau.dessiner_grille()


App()
