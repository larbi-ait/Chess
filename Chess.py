class Game:
    
    def __init__(self):
        self.plateau = self.creer_plateau()
    
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
        pass
        
    
chess = Game()

print(chess.afficher())