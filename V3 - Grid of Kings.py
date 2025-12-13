import pyxel

class Joueur :
    def __init__(self, JoueBlanc) :
        self.score = 0
        self.JoueBlanc = JoueBlanc
        self.echiquier = self.creer_echiquier()

    def creer_echiquier(self) :
        l = []
        if not self.JoueBlanc :
            for i in range(8) :
                l.append(Piece("PION", i, 1))
            l.append(Piece("CAVALIER", 1, 0))
            l.append(Piece("CAVALIER", 6, 0))
            l.append(Piece("TOUR", 0, 0))
            l.append(Piece("TOUR", 7, 0))
            l.append(Piece("FOU", 2, 0))
            l.append(Piece("FOU", 5, 0))
            l.append(Piece("DAME", 3, 0))
            l.append(Piece("ROI", 4, 0))
            return l
        else :
            for i in range(8) :
                l.append(Piece("PION", i, 6))
            l.append(Piece("CAVALIER", 1, 7))
            l.append(Piece("CAVALIER", 6, 7))
            l.append(Piece("TOUR", 0, 7))
            l.append(Piece("TOUR", 7, 7))
            l.append(Piece("FOU", 2, 7))
            l.append(Piece("FOU", 5, 7))
            l.append(Piece("DAME", 3, 7))
            l.append(Piece("ROI", 4, 7))
            return l

    def ajouter_score(self, score : int) :
        self.score += score

class Piece :
    def __init__(self, nom : str, x : int, y : int) :
        self.nom = nom
        self.x = x
        self.y = y

class Grille :
    def __init__(self) :
        self.plateau = self.creer_plateau()
        self.Taille_Cellule = 16

    def creer_plateau(self) :
        return [[0 for _ in range(8)] for _ in range(8)]

    def mettre_pieces(self, joueur : Joueur) :
        for i in joueur.echiquier :
            self.plateau[i.y][i.x] = i.nom



    def afficher_plateau(self) :
        for i in self.plateau :
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
        self.jeu = Grille()
        self.Joueur_Blanc = Joueur(True)
        self.Joueur_Noir = Joueur(False)

        pyxel.init(256, 256, title="Grid Of Kings")
        pyxel.run(self.update, self.draw)

    def dessiner_arriere_plan(self) :
        pyxel.rect(0, 0, 256, 256, 7)
        pyxel.rect(48, 48, 160, 160, 13)

    def update(self):
        self.jeu.afficher_plateau()
        self.jeu.mettre_pieces(self.Joueur_Noir)
        self.jeu.mettre_pieces(self.Joueur_Blanc)


    def draw(self):
        pyxel.cls(0)
        self.dessiner_arriere_plan()
        self.jeu.dessiner_grille()


App()
