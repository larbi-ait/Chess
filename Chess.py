import pyxel

class Piece :
    def __init__(self, nom : str, x : int, y : int, EstBlanc : bool) :
        self.nom = nom
        self.x = x
        self.y = y
        self.EstBlanc = EstBlanc
        self.first_case = True
        self.cases_atteignables = []

    def deplacement(self, coord):
        if coord in self.cases_atteignables:
            self.x, self.y = coord
            self.first_case = False
            if self.nom == "PION":
                if (self.EstBlanc and self.y == 0) or (not self.EstBlanc and self.y == 7):
                    self.promouvoir()
            return True
        return False

    def promouvoir(self):
        self.nom = "DAME"
        
    def on_board(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7
            
    def update_cases_atteignables(self, jeu):
        moves = []
        plateau = jeu.jeu.plateau
        if self.EstBlanc:
            ennemi = jeu.Joueur_Noir
        else:
            ennemi = jeu.Joueur_Blanc
        if self.nom == "PION":
            if self.EstBlanc:
                delta = [(0,-1),(0,-2),(-1,-1),(1,-1)]
            else:
                delta = [(0,1),(0,2),(1,1),(-1,1)]
            for dx, dy in delta:
                nx, ny = self.x + dx, self.y + dy
                if self.on_board(nx, ny):
                    if self.EstBlanc and dx == 0 and dy == -1 and plateau[ny][nx] == 0:
                        moves.append((nx, ny))
                    elif not self.EstBlanc and dx == 0 and dy == 1 and plateau[ny][nx] == 0:
                        moves.append((nx, ny))
                    elif self.first_case and dx == 0 and dy in [2,-2] and plateau[ny - 1][nx] == 0 and plateau[ny][nx] == 0:
                        moves.append((nx, ny))
                    elif dx != 0 and plateau[ny][nx] != 0 and plateau[ny][nx].EstBlanc != self.EstBlanc:
                        moves.append((nx, ny))
        if self.nom == "CAVALIER":
            delta = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
            for dx, dy in delta:
                nx, ny = self.x + dx, self.y + dy
                if self.on_board(nx, ny):
                    if plateau[ny][nx] == 0  or plateau[ny][nx].EstBlanc != self.EstBlanc:
                        moves.append((nx, ny))
        if self.nom == "TOUR" or self.nom == "DAME":
            delta = [(-1,0),(0,-1),(1,0),(0,1)]
            for dx, dy in delta:
                nx, ny = self.x + dx, self.y + dy
                stop = False
                while self.on_board(nx, ny) and not stop:
                    if plateau[ny][nx] == 0:
                        moves.append((nx, ny))
                        nx, ny = nx + dx, ny + dy
                    elif plateau[ny][nx].EstBlanc != self.EstBlanc:
                        moves.append((nx, ny))
                        stop = True
                    else:
                        stop = True
        if self.nom == "FOU" or self.nom == "DAME":
            delta = [(-1,-1),(1,-1),(1,1),(-1,1)]
            for dx, dy in delta:
                nx, ny = self.x + dx, self.y + dy
                stop = False
                while self.on_board(nx, ny) and not stop:
                    if plateau[ny][nx] == 0:
                        moves.append((nx, ny))
                        nx, ny = nx + dx, ny + dy
                    elif plateau[ny][nx].EstBlanc != self.EstBlanc:
                        moves.append((nx, ny))
                        stop = True
                    else:
                        stop = True
        if self.nom == "ROI":
            delta = [(-1,-1),(1,-1),(1,1),(-1,1),(-1,0),(0,-1),(1,0),(0,1)]
            cases_prises = []
            for i in ennemi.echiquier:
                if i.nom == "PION":
                    if self.EstBlanc:
                        cases_prises += [(i.x-1,i.y-1),(i.x+1,i.y-1)]
                    else:
                        cases_prises += [(i.x+1,i.y+1),(i.x-1,i.y+1)]
                elif i.nom == "ROI":
                    cases_prises += [(i.x-1,i.y-1),(i.x+1,i.y-1),(i.x+1,i.y+1),(i.x-1,i.y+1),(i.x-1,i.y+0),(i.x+0,i.y-1),(i.x+1,i.y+0),(i.x+0,i.y+1)]
                else:
                    cases_prises += i.cases_atteignables
            for dx, dy in delta:
                nx, ny = self.x + dx, self.y + dy
                if self.on_board(nx, ny):
                    if not (nx,ny) in cases_prises and (plateau[ny][nx] == 0  or plateau[ny][nx].EstBlanc != self.EstBlanc):
                        moves.append((nx,ny))
        self.cases_atteignables = moves
        return moves

class Joueur :
    def __init__(self, JoueBlanc) :
        self.score = 0
        self.coups = 0
        self.JoueBlanc = JoueBlanc
        self.echiquier = self.creer_echiquier()
        self.cases_controlees = []

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
        return self.score

    def nb_coups(self):
        self.coups += 1
        return self.coups

    def update_cases_controlees(self, jeu):
        self.cases_controlees = []
        for j in self.echiquier:
            self.cases_controlees += j.update_cases_atteignables(jeu)
        

class Grille :
    def __init__(self) :
        self.plateau = self.creer_plateau()
        self.Taille_Cellule = 16

    def creer_plateau(self) :
        return [[0 for _ in range(8)] for _ in range(8)]

    def mettre_pieces(self, joueur : Joueur) :
        for i in joueur.echiquier :
            self.plateau[i.y][i.x] = i

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
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 0, 16, 16, 16, 5)
                        else :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 0, 0, 16, 16, 5)
                    if piece.nom == "CAVALIER" :
                        if not piece.EstBlanc :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 16, 16, 16, 16, 5)
                        else :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 16, 0, 16, 16, 5)
                    if piece.nom == "FOU" :
                        if not piece.EstBlanc :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 32, 16, 16, 16, 5)
                        else :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 32, 0, 16, 16, 5)
                    if piece.nom == "TOUR" :
                        if not piece.EstBlanc :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 48, 16, 16, 16, 5)
                        else :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 48, 0, 16, 16, 5)
                    if piece.nom == "DAME" :
                        if not piece.EstBlanc :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 64, 16, 16, 16, 5)
                        else :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 64, 0, 16, 16, 5)
                    if piece.nom == "ROI" :
                        if not piece.EstBlanc :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 80, 16, 16, 16, 5)
                        else :
                            pyxel.blt(64 + j*16, 64 + i*16, 0, 80, 0, 16, 16, 5)
                            


class App:
    def __init__(self):
        self.jeu = Grille()
        self.Joueur_Blanc = Joueur(True)
        self.Joueur_Noir = Joueur(False)
        self.Joueur_Noir.update_cases_controlees(self)
        self.Joueur_Blanc.update_cases_controlees(self)
        self.current_player = self.Joueur_Blanc
        self.temps_blanc = 10 * 60  # 10 minutes
        self.temps_noir = 10 * 60
        self.piece_selectionnee = None

        pyxel.init(256, 256, title="Grid Of Kings")
        pyxel.load("gok.pyxres")
        pyxel.mouse(True)
        self.last_time = pyxel.frame_count
        self.en_pause = True
        pyxel.run(self.update, self.draw)

    def dessiner_pause(self):
        x, y = 120, 220

        if self.en_pause:
            
            pyxel.blt(x, y, 0, 16, 32, 16, 16, 5)
        else:
           
            pyxel.blt(x, y, 0, 32, 32, 16, 16, 5)
    
    def gerer_pause(self):
        x, y = 120, 220
        if x <= pyxel.mouse_x <= x + 16 and y <= pyxel.mouse_y <= y + 16:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.en_pause = not self.en_pause

    def update_temps(self):
        now = pyxel.frame_count
        delta_frames = now - self.last_time
        delta_seconds = delta_frames / 30
        if self.current_player.JoueBlanc:
            self.temps_blanc -= delta_seconds
            if self.temps_blanc < 0:
                self.temps_blanc = 0
        else:
            self.temps_noir -= delta_seconds
            if self.temps_noir < 0:
                self.temps_noir = 0

        self.last_time = now

    def interagir_piece(self, j : Piece) :
        if 64 + j.x * 16 <= pyxel.mouse_x < j.x*16 + 81 and 64 + j.y*16 <= pyxel.mouse_y < 81 + j.y*16 :
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and j.EstBlanc == self.current_player.JoueBlanc:
                self.piece_selectionnee = j
                    

    def interagir_plateau(self) :
        for i in self.jeu.plateau :
            for j in i :
                if j != 0 :
                    if 64 <= pyxel.mouse_x < 193 and 64 <= pyxel.mouse_y < 193 :
                        self.interagir_piece(j)
                        
    def deplacement(self):
        a_joue = False
        for y in range(8):
            for x in range(8):
                if 64 + x * 16 <= pyxel.mouse_x < x*16 + 81 and 64 + y*16 <= pyxel.mouse_y < 81 + y*16 :
                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                        if self.piece_selectionnee != None:
                            a_joue = self.piece_selectionnee.deplacement((x,y))
                            if a_joue:
                                if self.current_player.JoueBlanc:
                                    self.current_player = self.Joueur_Noir
                                else:
                                    self.current_player = self.Joueur_Blanc
                                piece_cible = self.jeu.plateau[y][x]
                                if piece_cible != 0:
                                    if piece_cible.EstBlanc:
                                        self.Joueur_Blanc.echiquier.remove(piece_cible)
                                    else:
                                        self.Joueur_Noir.echiquier.remove(piece_cible)

                                if self.current_player.JoueBlanc:
                                    self.Joueur_Blanc.nb_coups()
                                else:
                                    self.Joueur_Noir.nb_coups()
                        self.piece_selectionnee = None
        return a_joue

    def update(self):
        self.gerer_pause()
        if self.en_pause:
            return
        self.update_temps()
        self.jeu.plateau = self.jeu.creer_plateau()
        self.jeu.mettre_pieces(self.Joueur_Noir)
        self.jeu.mettre_pieces(self.Joueur_Blanc)
        if not self.deplacement():
            self.interagir_plateau()
        self.Joueur_Noir.update_cases_controlees(self)
        self.Joueur_Blanc.update_cases_controlees(self)

    def dessiner_piece_selectionnee(self) :
        if self.piece_selectionnee is not None:
            pyxel.rect(64 + self.piece_selectionnee.x*16, 64 + self.piece_selectionnee.y*16, 16, 16, 11)
            for x, y in self.piece_selectionnee.cases_atteignables:
                pyxel.circ(72 + x * 16, 72 + y * 16, 5, 13)
            

    def dessiner_arriere_plan(self) :
        pyxel.rect(0, 0, 256, 256, 7)
        pyxel.rect(48, 48, 160, 160, 13)
        pyxel.blt(5,25,0,0,32,16,16,5)

    def trait(self):
        if self.current_player.JoueBlanc:
            pyxel.text(100,20,"TRAIT AUX BLANCS", 0)
        else:
            pyxel.text(100,20,"TRAIT AUX NOIRS", 0)

        
    def afficher_temps(self):
        def format_time(t):
            t = int(t)
            return f"{t//60:02d}:{t%60:02d}"

        pyxel.text(30, 20, f"BLANC : {format_time(self.temps_blanc)}", 0)
        pyxel.text(30, 40, f"NOIR  : {format_time(self.temps_noir)}", 0)
        
    def afficher_coups(self):
        pyxel.text(150, 20, f"Coups BLANC : {self.Joueur_Blanc.coups}", 0)
        pyxel.text(150, 40, f"Coups NOIR  : {self.Joueur_Noir.coups}", 0)
    
    def draw(self):
        pyxel.cls(0)
        self.dessiner_arriere_plan()
        self.jeu.dessiner_grille()
        self.dessiner_piece_selectionnee()
        self.jeu.dessiner_pieces()
        self.trait()
        self.afficher_temps()
        self.afficher_coups()
        self.dessiner_pause()


App()






