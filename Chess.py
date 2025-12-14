import pyxel

class Piece :
    def __init__(self, nom : str, x : int, y : int, EstBlanc : bool) :
        self.nom = nom
        self.x = x
        self.y = y
        self.EstBlanc = EstBlanc
        self.first_case = True
        self.case_atteignable = []

    def deplacement(self, coord : (x, y)):
        if coord in self.case_atteignable:
            self.x, self.y = coord
            self.first_case = False
            
    def case_atteignable(self):
        moves = []
        if self.nom == "PION":
            pass
        if self.nom == "CAVALIER":
            pass
        if self.nom == "TOUR" or self.nom == "DAME":
            pass
        if self.nom == "FOU" or self.nom == "DAME":
            pass
        if self.nom == "ROI":
            pass
        

class Joueur :
    def __init__(self, JoueBlanc) :
        self.score = 0
        self.coups = 0
        self.JoueBlanc = JoueBlanc
        self.echiquier = self.creer_echiquier()

    def creer_echiquier(self) :
        l = []
        if not self.JoueBlanc :
            for i in range(8) :
                l.append(Piece("PION", i, 1, False))
            l.append(Piece("CAVALIER", 1, 0, False))
            l.append(Piece("CAVALIER", 6, 0, False))
            l.append(Piece("TOUR", 0, 0, False))
            l.append(Piece("TOUR", 7, 0, False))
            l.append(Piece("FOU", 2, 0, False))
            l.append(Piece("FOU", 5, 0, False))
            l.append(Piece("DAME", 3, 0, False))
            l.append(Piece("ROI", 4, 0, False))
            return l
        else :
            for i in range(8) :
                l.append(Piece("PION", i, 6, True))
            l.append(Piece("CAVALIER", 1, 7, True))
            l.append(Piece("CAVALIER", 6, 7, True))
            l.append(Piece("TOUR", 0, 7, True))
            l.append(Piece("TOUR", 7, 7, True))
            l.append(Piece("FOU", 2, 7, True))
            l.append(Piece("FOU", 5, 7, True))
            l.append(Piece("DAME", 3, 7, True))
            l.append(Piece("ROI", 4, 7, True))
            return l

    def ajouter_score(self, score : int) :
        self.score += score

    def nb_coups(self):
        self.coups += 1
        return self.coups
        

class Grille :
    def __init__(self) :
        self.plateau = self.creer_plateau()
        self.Taille_Cellule = 16

    def creer_plateau(self) :
        return [[0 for _ in range(8)] for _ in range(8)]

    def mettre_pieces(self, joueur : Joueur) :
        for i in joueur.echiquier :
            self.plateau[i.x][i.y] = i

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

    def dessiner_pieces(self) :
        for i in range(len(self.plateau)) :
            for j in range(len(self.plateau[i])) :
                piece = self.plateau[i][j]
                if type(piece) is not int :
                    if piece.nom == "PION" :
                        if not piece.EstBlanc :
                            pyxel.blt(64 + i*16, 64 + j*16, 0, 0, 16, 16, 16, 5)
                        else :
                            pyxel.blt(64 + i*16, 64 + j*16, 0, 0, 0, 16, 16, 5)
                    if piece.nom == "CAVALIER" :
                            if not piece.EstBlanc :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 16, 16, 16, 16, 5)
                            else :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 16, 0, 16, 16, 5)
                    if piece.nom == "FOU" :
                            if not piece.EstBlanc :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 32, 16, 16, 16, 5)
                            else :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 32, 0, 16, 16, 5)
                    if piece.nom == "TOUR" :
                            if not piece.EstBlanc :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 48, 16, 16, 16, 5)
                            else :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 48, 0, 16, 16, 5)
                    if piece.nom == "DAME" :
                            if not piece.EstBlanc :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 64, 16, 16, 16, 5)
                            else :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 64, 0, 16, 16, 5)
                    if piece.nom == "ROI" :
                            if not piece.EstBlanc :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 80, 16, 16, 16, 5)
                            else :
                                pyxel.blt(64 + i*16, 64 + j*16, 0, 80, 0, 16, 16, 5)



class App:
    def __init__(self):
        self.jeu = Grille()
        self.Joueur_Blanc = Joueur(True)
        self.Joueur_Noir = Joueur(False)
        for i in self.jeu.plateau:
            for j in i:
                if j != 0:
                    j.case_atteignable()
        self.piece_selectionnee = None

        pyxel.init(256, 256, title="Grid Of Kings")
        pyxel.load("gok.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)




    def interagir_piece(self, j : Piece) :
        if 64 + j.x * 16 <= pyxel.mouse_x < j.x*16 + 81 and 64 + j.y*16 <= pyxel.mouse_y < 81 + j.y*16 :
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
                self.piece_selectionnee = j

    def interagir_plateau(self) :
        for i in self.jeu.plateau :
            for j in i :
                if j != 0 :
                    if 64 <= pyxel.mouse_x < 193 and 64 <= pyxel.mouse_y < 193 :
                        if j != 0 :
                            self.interagir_piece(j)

    def update(self):
        self.jeu.mettre_pieces(self.Joueur_Noir)
        self.jeu.mettre_pieces(self.Joueur_Blanc)
        self.interagir_plateau()

    def dessiner_piece_selectionnee(self) :
        if self.piece_selectionnee is not None :
            pyxel.rect(64 + self.piece_selectionnee.x*16, 64 + self.piece_selectionnee.y*16, 16, 16, 11)

    def dessiner_arriere_plan(self) :
        pyxel.rect(0, 0, 256, 256, 7)
        pyxel.rect(48, 48, 160, 160, 13)

    def draw(self):
        pyxel.cls(0)
        self.dessiner_arriere_plan()
        self.jeu.dessiner_grille()
        self.dessiner_piece_selectionnee()
        self.jeu.dessiner_pieces()


App()
