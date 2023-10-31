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
    combat = 10
    vie = 3
    while vie > 0 and combat < 10: 
        if aventurier.pv > 0 or monstre.pv > 0:
            while r == "":
                r = input("1: ATTAQUER \n2: FUIR")
                if r == 1:
                    aventurier.attack(monstre)
                elif r == 2:
                    print("vous avez fuis le combat\n GAME OVER")
                    exit()
                else :
                    print("je n'est pas bien compris")
                monstre.attack(aventurier)
                break
        elif aventurier.pv <= 0:
            """"si les pv du joueurs tombent a 0 il perd un niveaux, ainsi qu'une vie"""
            print("Vous avez perdu, vous descendez de 1 niveaux.")
            aventurier.level_down()
            aventurier.pv = aventurier.pv_max
            vie -= 1
            print("il vous reste {vie} résurection disponible.")
        elif monstre.pv <= 0:
            aventurier.exp += monstre.XP
            combat += 1
            monstre = Ennemy()
            print(f"un nouveaux {monstre.name} apparait devant vous")
        else: 
            print("il y a eu une érreur lors du combat")
            break

        

        
    