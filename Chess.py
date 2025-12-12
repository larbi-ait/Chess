class Game:
    
    def __init__(self):
        self.plateau = self.creer_plateau()
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
        vide = 0
        pion = 1
        cavalier = 2
        fou = 3
        tour = 4
        dame = 5
        roi = 6
        self.plateau[0] = [tour, cavalier, fou, dame, roi, fou, cavalier, tour]
        self.plateau[1] = [pion] * 8
        self.plateau[6] = [pion] * 8
        self.plateau[7] = [tour, cavalier, fou, dame, roi, fou, cavalier, tour]
    
    
    
    
class Noir:
    pass

class Blanc:
    pass
        
    
chess = Game()

print(chess.afficher())
