# -*- coding: utf-8 -*-

# Définition des classes
class Employe:
    def __init__(self, identifiant, nom):
        self.id = identifiant
        self.nom = nom
        self.type = "Employé"
    
    def __repr__(self):
        chaine = "{} {} : {}".format(self.type, self.id, self.nom)
        return chaine
    
class Responsable(Employe):
    def __init__(self, identifiant, nom, rang):  
        Employe.__init__(self, identifiant, nom)
        self.type = "Responsable"
        self.number = rang
  
    def __repr__(self):
        chaine = "{} {} : {} (number {})".format(self.type, self.id, self.nom, self.number)
        return chaine
    
    def engueuler(self, employe):
        print("Alors, tu bosses un peu {} ou quoi ?!!".format(employe.nom))

# Programme principal
        
monEmploye = Employe("E001", "DURAND")
print(monEmploye)

monResponsable = Responsable("R001", "MARTIN", 2)
print(monResponsable)