class Game:
    
    def __init__(self):
        self.plateau = self.creer_plateau()
        self.noir = Noir()
        self.blanc = Blanc()
        self.placement()
    
    def creer_plateau(self):
        grille = []
        for i in range(8):
            eph = [0,0,0,0,0,0,0,0]
            grille.append(eph)
        return grille
    
    def afficher(self):
        for i in range(8):
            print(self.plateau[i])
    
    def placement(self):
        for x, y in self.noir.pieces:
            self.plateau[y][x] = self.noir.pieces[(x,y)]
        for x, y in self.blanc.pieces:
            self.plateau[y][x] = self.blanc.pieces[(x,y)]
    
class Noir:
    def __init__(self):
        self.pieces = {(0, 7) : 4, (1, 7) : 2, (2, 7) : 3, (3, 7) : 5, (4, 7) : 6, (5, 7) : 3, (6, 7) : 2, (7, 7) : 4,
                       (0, 6) : 1, (1, 6) : 1, (2, 6) : 1, (3, 6) : 1, (4, 6) : 1, (5, 6) : 1, (6, 6) : 1, (7, 6) : 1}
        self.possibilite_rock = True


class Blanc:
    def __init__(self):
        self.pieces = {(0, 0) : 4, (1, 0) : 2, (2, 0) : 3, (3, 0) : 5, (4, 0) : 6, (5, 0) : 3, (6, 0) : 2, (7, 0) : 4,
                       (0, 1) : 1, (1, 1) : 1, (2, 1) : 1, (3, 1) : 1, (4, 1) : 1, (5, 1) : 1, (6, 1) : 1, (7, 1) : 1}
        self.possibilite_rock = True
        
    
chess = Game()

print(chess.afficher())

