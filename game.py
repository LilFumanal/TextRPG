from Player import Player
from Ennemy import Ennemy

def creation_du_personage():
    nom = input(f"bonjour jeune aventurier, quelle est votre nom ? \n")
    print("{nom}, c'est ça ? bienvenue dans le donjon deathtrap")
    aventurier = Player(nom)
    return aventurier

def combat(aventurier): 
    monstre = Ennemy()   
    print(f"un {monstre.nom} apparait devant vous! Que faites-vous ?")
    r = input("1: ATTAQUER \n2: FUIR")
    if r == 1:
        aventurier.attack(monstre)
    elif r == 2:
        
